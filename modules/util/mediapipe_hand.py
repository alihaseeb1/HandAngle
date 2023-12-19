import tkinter as tk
from tkinter import Label, PhotoImage
import cv2
from PIL import Image, ImageTk
import modules.util.const as const
import mediapipe as mp


# メディアパイプによる手のランドマーク検出クラス
class HandLandmarkDetector:
    def __init__(self):
        # モデルの設定
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands()

    def detect(self, image):
        # 手のランドマーク検出
        results = self.hands.process(image)
        return results
