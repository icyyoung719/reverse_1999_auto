from task import Task
from button import Button

class DailyBattlePsy(Task):
    def run(self):
        try:
            self.wait_and_click(self.enter_the_show_button)
            self.wait_and_click(self.resource_button)
            self.wait_and_click(self.psy_free_text)
            self.wait_and_click(self.psy_07_btn)
            self.wait_and_click(self.start_action_button)

            if self.is_element_visible(self.replay_2_button, 0.95):
                self.wait_and_click(self.replay_2_times_button, timeout=30)
            else:
                self.wait_and_click(self.switch_replay_button)
                self.wait_and_click(self.replay_times_button)
                self.wait_and_click(self.replay_2_switch_button)
                self.wait_and_click(self.replay_2_times_button)

            self.wait_and_click(self.battle_win_info, 240)
            self.wait_and_click(self.back_to_home_button)
            return True
        except Exception as e:
            print(f"意志解析失败: {str(e)}")
            return False

    # 按钮定义
    enter_the_show_button = Button(name='enter_the_show_button', path='./assets/enter_the_show_button.png')
    resource_button = Button(name='resource_button', path='./assets/resource_button.jpg')
    psy_free_text = Button(name='psy_free_text', path='./assets/psy_free_times.png', offset=[0, -150])
    psy_07_btn = Button(name='psy_07_btn', path='./assets/psy_07_button.jpg')
    start_action_button = Button(name='start_action_button', path='./assets/start_action_button.jpg')
    replay_2_button = Button(name='replay_2_button', path='./assets/replay_2_button.png', min_similar=0.9)
    switch_replay_button = Button(name='switch_replay_button', path='./assets/switch_replay_button.jpg')
    replay_times_button = Button(name='replay_times_button', path='./assets/replay_times_button.jpg')
    replay_2_switch_button = Button(name='replay_2_switch_button', path='./assets/replay_2_switch_button.jpg')
    replay_2_times_button = Button(name='replay_2_times_button', path='./assets/replay_2_times_button.jpg')
    battle_win_info = Button(name='battle_win_info', path='./assets/battle_win_info.jpg')
    back_to_home_button = Button(name='back_to_home_button', path='./assets/back_to_home_button.png')