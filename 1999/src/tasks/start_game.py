from tasks.task import Task
from target.general import GameTarget
from engine.api import detect_image
from config.key.general import GeneralKey
from config.config import Config
import time
import subprocess
# import pyautogui

from log import Log
class StartGame(Task):
    gamePath = ""

    def __init__(self, path=None):
        # self.gamePath = path
        super().__init__(name="StartGame")
        self.gamePath = r'D:\1999\reverse1999_global\game\Reverse1999en\reverse1999.exe'

    def run(self):
        super().run()
        try:
            subprocess.Popen(self.gamePath)
            # 等待标题出现、
            # print("等待游戏启动")
            # time.sleep(5)
            self.wait_until_image_show(GameTarget.game_title, similarity=0.7)

            # 标题出现后，等待游戏完全响应
            print("等待游戏完全响应")
            time.sleep(Config.GAMETITLE_WAIT_TIME)
            self.wait_and_click(GameTarget.game_title, similarity=0.7)
            # 等待游戏进入
            # time.sleep(5)

            return True
        except Exception as e:
            print(f"游戏启动失败: {str(e)}")
            return False


class CloseNotice(Task):
    def __init__(self):
        super().__init__(name="CloseNotice")

    def run(self):
        super().run()
        try:
            # 不能这样，启动游戏后会有瞬间显示home_hide
            # while not self.detect_image(GameTarget.home_hide):
            #     time.sleep(Config.CLICK_INTERVAL)
            #     Log.press(GeneralKey.BACK_KEY)
            #     if self.detect_image(GameTarget.return_to_login):
            #         # ESC次数已经超过了，OCR略有失误

            #         # Log.press(GeneralKey.ENTER_KEY)
            #         # time.sleep(Config.CLICK_INTERVAL)
            #         time.sleep(Config.CLICK_INTERVAL)
            #         Log.press(GeneralKey.BACK_KEY)
            #         print("ESC次数已经超过了，OCR略有失误")
            #         break
            while not self.detect_image(GameTarget.return_to_login):
                time.sleep(Config.CLICK_INTERVAL)
                Log.press(GeneralKey.BACK_KEY)

            # 防止再次弹出公告，再次重复一次
            time.sleep(Config.CLICK_INTERVAL)
            while not self.detect_image(GameTarget.return_to_login):
                time.sleep(Config.CLICK_INTERVAL)
                Log.press(GeneralKey.BACK_KEY)
            
            time.sleep(Config.CLICK_INTERVAL)
            Log.press(GeneralKey.BACK_KEY)
            time.sleep(Config.CLICK_INTERVAL)

            print("进入主界面")
            return True
            
        except Exception as e:
            print(f"关闭公告失败: {str(e)}")
            return False
        
    

    




