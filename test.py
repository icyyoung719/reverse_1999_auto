import time

from utils import click_on_image, wait_until_image_show, detect_image


class Button:
    name = None
    path = None
    offset = None
    default_min_similar = 0.5

    def __init__(self, name, path, min_similar=default_min_similar, offset=None):
        self.name = name
        self.path = path
        self.min_similar = min_similar
        if self.min_similar is None:
            self.min_similar = 0.8
        self.offset = offset

    def click(self):
        print(f"{self.name} clicked")
        return click_on_image(self.path, similar=self.min_similar, click_offset=self.offset)


window_button = Button("window", "./assets/windows.jpg")
game_button = Button("game", "./assets/reverse_1999.png")


def test_windows_button():
    game_button.click()


if __name__ == "__main__":
    test_windows_button()