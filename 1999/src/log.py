import pyautogui

class Log:
    def press(self, key):
        print(f'{{"key": "{key}"}} pressed')
        pyautogui.press(key)