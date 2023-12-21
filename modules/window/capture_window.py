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

    def capture_image(self):
        self.create_directory("capture_img")
        filename = f"capture_Pose{int(self.i)}.jpg"
        self.save_path = os.path.join(self.current_dir, "capture_img", filename)
        cv2.imwrite(self.save_path, self.frame)

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
