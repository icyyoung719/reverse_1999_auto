from task import Task
from button import Button

class DailyMissionCollect(Task):
    def run(self):
        try:
            # 主界面入口
            self.wait_and_click(self.main_quest_button)
            
            # 进入每日任务界面
            self.wait_and_click(self.daily_mission_tab)
            
            # 领取已完成任务奖励
            if self.is_element_visible(self.claim_all_button):
                self.wait_and_click(self.claim_all_button)
                self.wait_and_click(self.confirm_claim_button)
            
            # 返回主界面
            self.wait_and_click(self.back_to_home_button)
            return True
        except Exception as e:
            print(f"每日任务领取失败: {str(e)}")
            return False

    # 按钮定义
    main_quest_button = Button(name='main_quest', path='./assets/main_quest_button.jpg')
    daily_mission_tab = Button(name='daily_mission_tab', path='./assets/daily_mission_tab.png')
    claim_all_button = Button(name='claim_all', path='./assets/claim_all_button.jpg', min_similar=0.9)
    confirm_claim_button = Button(name='confirm_claim', path='./assets/confirm_claim_button.jpg')
    back_to_home_button = Button(name='back_to_home', path='./assets/back_to_home_button.png')