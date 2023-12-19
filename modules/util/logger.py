import logging
import datetime
import os
from modules.util import const


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        if not hasattr(self, "initialized"):
            # Ensure the base log directory exists
            if not os.path.exists(const.LOG_PATH):
                os.makedirs(const.LOG_PATH)

            # Create a directory structure based on the current datetime
            current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            self.current_log_dir = os.path.join(const.LOG_PATH, current_time)

            # Ensure the log directory exists
            if not os.path.exists(self.current_log_dir):
                os.makedirs(self.current_log_dir)

            # Ensure the image directory exists
            self.img_path = os.path.join(self.current_log_dir, "img")
            if not os.path.exists(self.img_path):
                os.makedirs(self.img_path)

            # Create log filename
            log_filename = os.path.join(self.current_log_dir, f"log_{current_time}.log")

            # Set up logging as before
            self.logger = logging.getLogger(self.__class__.__name__)
            self.logger.setLevel(logging.DEBUG)

            fh = logging.FileHandler(log_filename)
            fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            self.logger.addHandler(fh)

            ch = logging.StreamHandler()
            ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            self.logger.addHandler(ch)

            self.initialized = True

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def save_image(self, frame, img_name=None):
        # If img_name isn't provided, use the current time as the filename
        if img_name is None:
            file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f") + ".jpg"  # %f is microseconds
        else:
            file_name = (
                datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f") + "_" + img_name + ".jpg"
            )  # %f is microseconds
        img_path = os.path.join(self.img_path, file_name)
        cv2.imwrite(img_path, frame)
