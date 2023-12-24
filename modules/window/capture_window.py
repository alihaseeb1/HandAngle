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
        self.right_hand = True
        self.left_hand = True

        # 検出器のセットアップ
        self.hand_detector = HandLandmarkDetector()

        # GUIセットアップ
        self.setup_background()
        self.setup_display_explanation()
        self.setup_camera()
        self.setup_buttons()

        # カメラ映像の表示
        self.camera_label = Label(self)  # カメラ映像を表示するLabelウィジェット
        self.camera_label.place(x=1050, y=400)

        # 指示画像の表示
        self.instraction_label = Label(self)
        self.instraction_label.place(x=250, y=400)

        # 最初のカメラをデフォルトとして使用
        self.capture = cv2.VideoCapture(self.cameras[0][0])

        self.display_instraction_img()

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
        ただし、次の文が実際に存在する場合のみ、改行を追加します。
        """
        parts = text.split(delimiter)
        processed_parts = []

        for i, part in enumerate(parts[:-1]):
            part = part.strip()
            # 次の部分が存在し、非空である場合にのみ、改行を追加
            if part and (i + 1 < len(parts) and parts[i + 1].strip()):
                processed_parts.append(part + delimiter + "\n")
            else:
                processed_parts.append(part + delimiter)
        processed_parts.append(parts[-1].strip())  # 最後の部分をそのまま追加

        return "".join(processed_parts)

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

        if not hasattr(self, "explanation_label"):
            self.explanation_label = Label(
                self,
                bg=const.DISPLAY_EXPLANATION_BG,
                fg=const.DISPLAY_EXPLANATION_FG,
                font=const.DISPLAY_EXPLANATION_2_FONT,
            )
            self.explanation_label.pack(
                pady=(const.DISPLAY_EXPLANATION_MENU_LABEL_IPADY + 50, 0),
                ipadx=10,
            )

        # 右手/左手ラベルの作成と配置
        if not hasattr(self, "hand_label"):
            self.hand_label = Label(
                self,
                bg=const.DISPLAY_EXPLANATION_BG,
                fg=const.DISPLAY_EXPLANATION_FG,
                font=const.DISPLAY_EXPLANATION_FONT,
            )
            self.hand_label.pack(pady=(10, 0))

        # self.iの値に応じてラベルのテキストを更新
        if self.i <= 35:
            menu_text = const.DISPLAY_POSE_NUMBER[self.i]
            explanation_text = const.DISPLAY_EXPLANATION_NUMBER[self.i]
        elif 36 <= self.i <= 71:
            # 36から71の範囲では、0からのインデックスを使用
            menu_text = const.DISPLAY_POSE_NUMBER[self.i - 36]
            explanation_text = const.DISPLAY_EXPLANATION_NUMBER[self.i - 36]
        else:
            # self.iが72以上の場合
            menu_text = "FINISH!"
            explanation_text = "THANK YOU"

        self.menu_label.config(text=menu_text)
        processed_text = self.insert_newlines(explanation_text)
        self.explanation_label.config(text=processed_text)

        # self.iの値に応じて右手/左手ラベルのテキストを設定
        if self.i <= 35:
            self.hand_label.config(text="RIGHT HAND")
        elif 36 <= self.i <= 71:
            self.hand_label.config(text="LEFT HAND")
        else:
            # 71を超えた際にラベルを削除
            self.hand_label.config(text="")

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
            text="Back ",
            command=self.back_pose,
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
        filename = f"{self.i}.jpg"
        instraction_img = cv2.imread(os.path.join(self.current_dir, "data", filename))
        instraction_img = cv2.cvtColor(instraction_img, cv2.COLOR_BGR2RGB)

        # 画像のサイズを4分の1にする
        height, width = instraction_img.shape[:2]
        instraction_img = cv2.resize(instraction_img, (width // 3, height // 3))

        instraction_img_2 = Image.fromarray(instraction_img)
        instraction_photo = ImageTk.PhotoImage(image=instraction_img_2)
        self.instraction_label.config(image=instraction_photo)
        self.instraction_label.image = instraction_photo

    def capture_image(self):
        self.create_directory("to_process")
        filename = f"{int(self.i)}.jpg"
        self.save_path = os.path.join(self.current_dir, "to_process", filename)
        cv2.imwrite(self.save_path, self.frame)
        self.i += 1
        self.setup_display_explanation()
        self.display_instraction_img()

    def create_directory(self, dir_name):
        dir_path = os.path.join(self.current_dir, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def setup_camera(self):
        self.cameras = camera_setup.get_cameras()
        return self.cameras[0][0]

    def back_pose(self):
        self.i -= 1
        self.setup_display_explanation()
        self.display_instraction_img()

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
