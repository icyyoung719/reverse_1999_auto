import time
from abc import ABC, abstractmethod

from engine.api import wait_until_image_show, detect_image
from target.target import Target
from config.config import Config

class Task(ABC):
    def __init__(self, name=None):
        self.name = name or self.__class__.__name__
    def wait_and_click(self, target: Target, similarity = Config.MIN_SIMILARITY, timeout=30):
        wait_until_image_show(target.path, similarity, timeout)
        time.sleep(Config.CLICK_AFTER_WAIT)
        return target.click()

    def detect_image(self, target: Target):
        return detect_image(target.path)
    
    def wait_until_image_show(self, target: Target, similarity = Config.MIN_SIMILARITY, timeout=30):
        return wait_until_image_show(target.path, similarity, timeout)

    def run(self):
        print(f"===== Task Begin: {self.name} =====")