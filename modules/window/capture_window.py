import tkinter as tk
from tkinter import Button, Label, PhotoImage, Listbox
from modules.util.mediapipe_hand import HandLandmarkDetector
from PIL import Image, ImageTk
import modules.window.const as const
import modules.util.const_logger as const_logger
import modules.util.camera_setup as camera_setup
import os
import cv2
import time
import csv


class CaptureWindow(tk.Frame):
    def __init__(self, master, i):
        super().__init__(master)
        self.master = master
        self.master.logger.info(const_logger.CAPTURE_WINDOW_START_MSG)
        self.current_dir = os.getcwd()
        self.i = i

        # 検出器のセットアップ
        self.hand_detector = HandLandmarkDetector()

        # GUIセットアップ
        self.setup_background()
        self.setup_display_explanation()
        self.setup_camera()
        self.setup_buttons()

        # カメラ映像の表示
        self.camera_label = Label(self)  # カメラ映像を表示するLabelウィジェット
        self.camera_label.place(x=1050, y=350)

        # 指示画像の表示
        self.instraction_img = Label(self)
        self.instraction_img.place(x=350, y=350)

        # 最初のカメラをデフォルトとして使用
        self.capture = cv2.VideoCapture(self.cameras[0][0])
        # カメラ映像の更新
        self.update_camera()

    def setup_background(self):
        # 背景画像のセットアップ
        self.bg_image = PhotoImage(file=os.path.join(self.current_dir, const.BG_IMAGE_PATH))
        bg_label = Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

    def insert_newlines(self, text, delimiter="."):
        """
        指定されたデリミター（デフォルトはピリオド）でテキストを分割し、
        各部分を改行で結合して返します。
        """
        parts = text.split(delimiter)
        # デリミターを各部分の末尾に再追加（最後の部分を除く）
        processed_parts = [part + delimiter for part in parts[:-1]]
        processed_parts.append(parts[-1])  # 最後の部分をそのまま追加
        return "\n".join(processed_parts)

    def setup_display_explanation(self):
        if not hasattr(self, "menu_label"):
            # ラベルがまだ作成されていない場合、新しく作成します
            self.menu_label = Label(
                self,
                bg=const.DISPLAY_EXPLANATION_BG,
                fg=const.DISPLAY_EXPLANATION_FG,
                font=const.DISPLAY_EXPLANATION_FONT,
            )
            self.menu_label.pack(
                pady=const.DISPLAY_EXPLANATION_MENU_LABEL_IPADY, ipadx=const.DISPLAY_EXPLANATION_MENU_LABEL_IPADX
            )
        # ラベルのテキストを更新します
        self.menu_label.config(text=const.DISPLAY_POSE_NUMBER[self.i])

        # ラベルのテキストを設定する際に、新しい関数を使用
        if not hasattr(self, "explanation_label"):
            self.explanation_label = Label(
                self,
                bg=const.DISPLAY_EXPLANATION_BG,
                fg=const.DISPLAY_EXPLANATION_FG,
                font=const.DISPLAY_EXPLANATION_2_FONT,
                # widthオプションはコメントアウト
            )
            self.explanation_label.pack(
                pady=(const.DISPLAY_EXPLANATION_MENU_LABEL_IPADY + 50, 0),
                ipadx=10,
                # fillオプションはコメントアウト
            )

        # テキストを改行で処理してから設定
        processed_text = self.insert_newlines(const.DISPLAY_EXPLANATION_NUMBER[self.i])
        self.explanation_label.config(text=processed_text)

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

        # Settingボタンのセットアップ
        Button(
            self,
            text="Setting",
            command=self.open_setting,
            font=const.CAPTURE_BUTTON_FONT,
            width=const.CAPTURE_BUTTON_WIDTH,
            height=const.CAPTURE_BUTTON_HEIGHT,
        ).place(relx=0.8, rely=1.0, x=-const.CAPTURE_BUTTON_PADX, y=-const.CAPTURE_BUTTON_PADY, anchor=tk.SE)

    def update_camera(self):
        ret, self.frame = self.capture.read()
        if ret:
            self.process_camera_frame()
        self.after(10, self.update_camera)

    def process_camera_frame(self):
        self.display_camera_frame()

    def display_camera_frame(self):
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        self.camera_label.config(image=photo)
        self.camera_label.image = photo

    def display_instraction_img(self):
        cv2.imread(os.path.join(self.current_dir, const.INSTRACTION_IMAGE_PATH))

    def capture_image(self):
        self.create_directory("capture_img")
        filename = f"capture_Pose{int(self.i)}.jpg"
        self.save_path = os.path.join(self.current_dir, "capture_img", filename)
        cv2.imwrite(self.save_path, self.frame)
        self.i += 1
        self.setup_display_explanation()

    def create_directory(self, dir_name):
        dir_path = os.path.join(self.current_dir, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def setup_camera(self):
        self.cameras = camera_setup.get_cameras()
        return self.cameras[0][0]

    def open_setting(self):
        # カメラ設定ウィンドウの作成
        setting_window = tk.Toplevel(self)
        setting_window.title("Camera Settings")

        # 使用可能なカメラの一覧を取得
        cameras = camera_setup.get_cameras()

        # カメラの一覧を表示するListboxの作成
        camera_listbox = Listbox(setting_window)
        for cam_id, cam_name in cameras:
            camera_listbox.insert(tk.END, f"Camera {cam_id}: {cam_name}")
        camera_listbox.pack()

        # 選択ボタンの作成
        Button(setting_window, text="Select", command=lambda: self.select_camera(camera_listbox, cameras)).pack()
