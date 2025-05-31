import time

from tasks.task import Task
from target.target import Target
from target.general import GameTarget

from config.key.homepage import HomepageKey
from config.config import Config

from log import Log

class DailyMissionCollect(Task):
    def __init__(self):
        super().__init__(name='Daily Mission Collect')

    def run(self):
        super().run()
        try:
            Log.press(HomepageKey.TASKS_KEY)
            time.sleep(Config.CLICK_AFTER_WAIT)
            if self.detect_image(GameTarget.collect_tasks):
                self.wait_and_click(GameTarget.collect_tasks)
                self.wait_and_click(GameTarget.confirm_collect)
            
            self.wait_and_click(GameTarget.back_to_home)
            return True
            # TODO:添加周任务领取、点唱机领取
        
        except Exception as e:
            Log.error(f"每日任务领取失败: {str(e)}")
            return False

class DailyRoarJukeboxCollect(Task):
    def __init__(self):
        super().__init__(name='Daily Roar Jukebox Collect')
    
    def run(self):
        super().run()
        try:
            Log.press(HomepageKey.ROAR_JUNKBOX_KEY)
            time.sleep(Config.CLICK_AFTER_WAIT)
            if self.detect_image(GameTarget.collect_roar_jukebox):
                self.wait_and_click(GameTarget.collect_roar_jukebox)
                time.sleep(Config.CLICK_AFTER_WAIT)
                if self.detect_image(GameTarget.roar_jukebox_update):
                    self.wait_and_click(GameTarget.roar_jukebox_update)
                    time.sleep(Config.CLICK_AFTER_WAIT)
            
            self.wait_and_click(GameTarget.back_to_home)
            return True

        except Exception as e:
            Log.error(f"Roar Box领取失败: {str(e)}")
            return False


# class DailyMissionCollect(Task):
#     def run(self):
#         try:
#             # 主界面入口
#             self.wait_and_click(self.main_quest_button)
            
#             # 进入每日任务界面
#             self.wait_and_click(self.daily_mission_tab)
            
#             # 领取已完成任务奖励
#             if self.is_element_visible(self.claim_all_button):
#                 self.wait_and_click(self.claim_all_button)
#                 self.wait_and_click(self.confirm_claim_button)
            
#             # 返回主界面
#             self.wait_and_click(self.back_to_home_button)
#             return True
#         except Exception as e:
#             print(f"每日任务领取失败: {str(e)}")
#             return False

#     # 按钮定义
#     main_quest_button = Button(name='main_quest', path='./assets/main_quest_button.jpg')
#     daily_mission_tab = Button(name='daily_mission_tab', path='./assets/daily_mission_tab.png')
#     claim_all_button = Button(name='claim_all', path='./assets/claim_all_button.jpg', min_similar=0.9)
#     confirm_claim_button = Button(name='confirm_claim', path='./assets/confirm_claim_button.jpg')
#     back_to_home_button = Button(name='back_to_home', path='./assets/back_to_home_button.png')