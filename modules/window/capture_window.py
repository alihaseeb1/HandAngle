import tkinter as tk
from tkinter import Button, Label, PhotoImage, simpledialog
from modules.util.mediapipe_hand import HandLandmarkDetector
from PIL import Image, ImageTk
import modules.window.const as const
import modules.util.const_logger as const_logger
import modules.util.camera_setup as camera_setup
import os
import cv2
import time


class CaptureWindow(tk.Frame):
    def __init__(self, master, i):
        super().__init__(master)
        self.master = master
        self.master.logger.info(const_logger.CAPTURE_WINDOW_START_MSG)
        self.current_dir = os.getcwd()
        self.i = i

        # 検出器のセットアップ
        self.hand_detector = HandLandmarkDetector()
        self.detect_hands = False

        # GUIセットアップ
        self.setup_background()
        self.setup_display_explanation()
        self.setup_camera()
        self.setup_buttons()

        # カメラ映像の表示
        self.camera_label = Label(self)  # カメラ映像を表示するLabelウィジェット
        self.camera_label.place(x=800, y=150)

        # 最初のカメラをデフォルトとして使用
        self.capture = cv2.VideoCapture(self.cameras[0][0])

        # カメラ映像の更新
        self.update_camera()

    def setup_background(self):
        # 背景画像のセットアップ
        self.bg_image = PhotoImage(file=os.path.join(self.current_dir, const.BG_IMAGE_PATH))
        bg_label = Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

    def setup_display_explanation(self):
        # 画面説明のセットアップ
        menu_label = Label(
            self,
            text=const.DISPLAY_EXPLANATION[self.i],
            bg=const.DISPLAY_EXPLANATION_BG,
            fg=const.DISPLAY_EXPLANATION_FG,
            font=const.DISPLAY_EXPLANATION_FONT,
        )
        menu_label.pack(
            pady=const.DISPLAY_EXPLANATION_MENU_LABEL_IPADY, ipadx=const.DISPLAY_EXPLANATION_MENU_LABEL_IPADX
        )

    def setup_buttons(self):
        # Captureボタンのセットアップ
        Button(
            self,
            text="Capture",
            command=self.capture_image,
            font=const.CAPTURE_BUTTON_FONT,
            width=const.CAPTURE_BUTTON_WIDTH,
            height=const.CAPTURE_BUTTON_HEIGHT,
        ).place(relx=1.0, rely=1.0, x=-const.CAPTURE_BUTTON_PADX, y=-const.CAPTURE_BUTTON_PADY, anchor=tk.SE)

    def update_camera(self):
        # カメラからフレームを読み込む
        ret, self.frame = self.capture.read()
        if ret:
            if self.detect_hands:
                # 手のランドマーク検出
                results = self.hand_detector.detect(self.frame)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        self.hand_detector.mp_drawing.draw_landmarks(
                            self.frame, hand_landmarks, self.hand_detector.mp_hands.HAND_CONNECTIONS
                        )

            # OpenCVのBGR画像をRGBに変換
            frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            # Tkinterで表示可能な形式に変換
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=image)

            # Labelウィジェットに画像を設定
            self.camera_label.config(image=photo)
            self.camera_label.image = photo  # 参照を保持

        # 次のフレームを取得するために自身を再呼び出し
        self.after(10, self.update_camera)

    def capture_image(self):
        # capture_imgディレクトリのパス
        capture_dir = os.path.join(self.current_dir, "capture_img")

        # ディレクトリが存在しない場合は作成
        if not os.path.exists(capture_dir):
            os.makedirs(capture_dir)

        # ファイル名は現在のタイムスタンプを使用
        filename = f"capture_Pose{int(self.i)}.jpg"
        self.save_path = os.path.join(capture_dir, filename)
        cv2.imwrite(self.save_path, self.frame)

        self.master.show_detection_window(self.save_path, self.i)

    def setup_camera(self):
        self.cameras = camera_setup.get_cameras()
