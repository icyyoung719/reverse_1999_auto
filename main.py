import sys
import time

from function import *
from utils import save_json,load_json
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtCore import Slot
from ui import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.game_path = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_click_run_btn)
        self.ui.pushButton_2.clicked.connect(self.on_select_file_name)
        self.function_to_complete = [False, False, False, False, False]

    def runHelper(self):
        if self.function_to_complete[0]:
            if game_path:
                path_start_game(game_path)
            else:
                path_start_game()
            time.sleep(8)
        else:
            find_game()
            time.sleep(2)
        if self.function_to_complete[1]:
            wilderness_collect()
        if self.function_to_complete[2]:
            time.sleep(3)
            daily_battle_psy()
        if self.function_to_complete[3]:
            the_poussiere()
        if self.function_to_complete[4]:
            daily_task_claim()

    def on_click_run_btn(self):
        self.function_to_complete[0] = self.ui.checkBox.isChecked()
        self.function_to_complete[1] = self.ui.checkBox_2.isChecked()
        self.function_to_complete[2] = self.ui.checkBox_3.isChecked()
        self.function_to_complete[3] = self.ui.checkBox_4.isChecked()
        self.function_to_complete[4] = self.ui.checkBox_5.isChecked()
        self.save_user_config()
        time.sleep(0.5)

        self.runHelper()

    def on_select_file_name(self):
        self.game_path = QFileDialog.getOpenFileName(self, "Open File",
                                                     "/home",
                                                     "EXE (*.exe)")

        if self.game_path:
            return True
        else:
            return False

    def save_user_config(self):
        config_data = {
            "game_path": self.game_path,
            "last_function_select": self.function_to_complete,
        }
        save_json(config_data)

    def load_user_config(self):
        config_data = load_json()
        if config_data:
            self.game_path = config_data["game_path"]
            self.function_to_complete = config_data["last_function_select"]
            self.ui.checkBox.setChecked(self.function_to_complete[0])
            self.ui.checkBox_2.setChecked(self.function_to_complete[1])
            self.ui.checkBox_3.setChecked(self.function_to_complete[2])
            self.ui.checkBox_4.setChecked(self.function_to_complete[3])
            self.ui.checkBox_5.setChecked(self.function_to_complete[4])
        else:
            return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.load_user_config()
    myWindow.show()

    sys.exit(app.exec())
