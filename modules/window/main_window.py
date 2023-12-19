import tkinter as tk
from modules.window.capture_window import CaptureWindow
from modules.window.detection_window import DetectionWindow
import modules.util.const_logger as const_logger
from modules.util.logger import Logger


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logger = Logger()
        self.logger.info(const_logger.START_MEG)

        # ウィンドウをフルスクリーンに設定
        self.attributes("-fullscreen", True)

        # 初期ウインドウの表示
        self.current_frame = None
        self.show_capture_window(i=0)

    def on_close(self):
        """ウィンドウを閉じる際の処理"""
        self.logger.info(const_logger.FINISH_MEG)
        self.destroy()

    def show_window(self, window_class, *args, **kwargs):
        # 指定されたウィンドウクラスを表示する汎用メソッド
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = window_class(self, *args, **kwargs)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_capture_window(self, i):
        # キャプチャー画面を表示する
        self.show_window(CaptureWindow, i)

    def show_detection_window(self, save_path, i):
        # 検出画面を表示する
        self.show_window(DetectionWindow, save_path, i)
