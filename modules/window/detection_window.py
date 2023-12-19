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
import mediapipe as mp
import numpy as np
import csv


class DetectionWindow(tk.Frame):
    def __init__(self, master, save_path, i):
        super().__init__(master)
        self.master = master
        self.master.logger.info(const_logger.DETECTION_WINDOW_START_MSG)

        # 検出器のセットアップ
        self.hand_detector = HandLandmarkDetector()
        
        # 画像の保存先
        self.save_path = save_path
        self.current_dir = os.getcwd()

        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils

        # GUIセットアップ
        self.setup_background()
        self.setup_buttons()
        self.display_detection_result(i)

    def setup_background(self):
        # 背景画像のセットアップ
        self.bg_image = PhotoImage(file=os.path.join(self.current_dir, const.BG_IMAGE_PATH))
        bg_label = Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

    def setup_buttons(self):
        # Captureボタンのセットアップ
        Button(
            self,
            text="Next",
            command=self.go_to_capture_window,
            font=const.CAPTURE_BUTTON_FONT,
            width=const.CAPTURE_BUTTON_WIDTH,
            height=const.CAPTURE_BUTTON_HEIGHT,
        ).place(relx=1.0, rely=1.0, x=-const.CAPTURE_BUTTON_PADX, y=-const.CAPTURE_BUTTON_PADY, anchor=tk.SE)

    def display_detection_result(self, i):
        # Save poses as csv
        # print(poses.shape)
        os.makedirs("output", exist_ok=True)

        # カメラ映像の表示
        self.detection_label = Label(self)  # カメラ映像を表示するLabelウィジェット
        self.detection_label.place(x=800, y=150)
        # 検出結果を表示する
        self.capture_img = cv2.imread(self.save_path)
        self.capture_img = cv2.cvtColor(self.capture_img, cv2.COLOR_BGR2RGB)
        self.detection_img = self.capture_img
        detection_result = self.hand_detector.detect(self.detection_img)

        if detection_result.multi_hand_landmarks:
            for hand_no, hand_landmarks in enumerate(detection_result.multi_hand_landmarks):
                # landmarks.csvが存在するかチェック
                file_exists = os.path.exists(f"output/landmarks.csv")

                with open(f"output/landmarks.csv", "a", newline="") as f:
                    csv_writer = csv.writer(f)

                    if not file_exists:
                        # ヘッダー行の生成と書き込み
                        axis = ["x", "y", "z"]
                        cols = ["Joint_" + str(col) + "_" + axis[x] for col in range(21) for x in range(3)]
                        header = ["Pose"] + cols
                        csv_writer.writerow(header)

                    # データ行の書き込み
                    row_data = [i]  # 最初の列にポーズ番号を追加
                    for k in range(21):
                        row_data.extend(
                            [
                                hand_landmarks.landmark[k].x,
                                hand_landmarks.landmark[k].y,
                                hand_landmarks.landmark[k].z,
                            ]
                        )
                    csv_writer.writerow(row_data)
                self.mp_drawing.draw_landmarks(self.detection_img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        # Tkinerで表示可能な形式に変換
        image = Image.fromarray(self.detection_img)
        photo = ImageTk.PhotoImage(image=image)

        # Labelウィジェットに画像を設定
        self.detection_label.config(image=photo)
        self.detection_label.image = photo  # 参照を保持

        detection_dir = os.path.join(self.current_dir, "detection_img")
        if not os.path.exists(detection_dir):
            os.mkdir(detection_dir)

        filename = f"detection_pose{int(i)}.jpg"
        self.save_path = os.path.join(detection_dir, filename)
        cv2.imwrite(self.save_path, cv2.cvtColor(self.detection_img, cv2.COLOR_RGB2BGR))

        self.j = i + 1

    def go_to_capture_window(self):
        self.master.show_capture_window(self.j)
