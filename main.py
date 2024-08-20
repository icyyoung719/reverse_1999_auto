import sys
from function import *
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot
from ui import Ui_MainWindow

class MainWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_click_run_btn)
        self.function_to_complete = [False,False,False,False,False]

    def runHelper(self):
        if self.function_to_complete[0]:
            path_start_game()
        if self.function_to_complete[1]:
            wildren_collect()
        if self.function_to_complete[2]:
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

        self.runHelper()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()

    sys.exit(app.exec())