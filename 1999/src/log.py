import pyautogui

class Log:
    @staticmethod
    def press(key):
        print(f"{key} pressed")
        pyautogui.press(key)