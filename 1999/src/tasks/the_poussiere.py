from task import Task
from button import Button

class ThePoussiere(Task):
    def run(self):
        try:
            self.wait_and_click(self.enter_the_show_button)
            self.wait_and_click(self.resource_button)
            self.wait_and_click(self.the_poussiere_button)
            self.wait_and_click(self.resource_06_button)
            self.wait_and_click(self.start_action_button)

            if self.is_element_visible(self.replay_4_button, 0.95):
                self.wait_and_click(self.replay_4_times_button, timeout=30)
            else:
                self.wait_and_click(self.switch_replay_button)
                self.wait_and_click(self.replay_times_button)
                self.wait_and_click(self.replay_4_switch_button)
                self.wait_and_click(self.replay_4_times_button)

            self.wait_and_click(self.battle_win_info, 240)
            self.wait_and_click(self.back_to_home_button)
            return True
        except Exception as e:
            print(f"微尘收集失败: {str(e)}")
            return False

    # 专属按钮定义
    enter_the_show_button = Button(name='enter_the_show_button', path='./assets/enter_the_show_button.png')
    resource_button = Button(name='resource_button', path='./assets/resource_button.jpg')
    the_poussiere_button = Button(name='the_poussiere_button', path='./assets/the_poussiere_button.jpg')
    resource_06_button = Button(name='resource_06_button', path='./assets/resource_06_button.jpg')
    start_action_button = Button(name='start_action_button', path='./assets/start_action_button.jpg')
    replay_4_button = Button(name='replay_4_button', path='./assets/replay_4_button.jpg', min_similar=0.9)
    switch_replay_button = Button(name='switch_replay_button', path='./assets/switch_replay_button.jpg')
    replay_times_button = Button(name='replay_times_button', path='./assets/replay_times_button.jpg')
    replay_4_switch_button = Button(name='replay_4_switch_button', path='./assets/replay_4_switch_button.jpg')
    replay_4_times_button = Button(name='replay_4_times_button', path='./assets/replay_4_times_button.jpg')
    battle_win_info = Button(name='battle_win_info', path='./assets/battle_win_info.jpg')
    back_to_home_button = Button(name='back_to_home_button', path='./assets/back_to_home_button.png')