# import pyautogui
import time

from tasks.task import Task
from target.target import Target
from target.general import GameTarget

from config.key.wildness import WildnessKey
from config.key.homepage import HomepageKey
from config.key.general import GeneralKey
from config.config import Config

from log import Log

class WildernessCollect(Task):
    def __init__(self):
        super().__init__(name="WildernessCollect")

    def run(self):
        super().run()
        try:
            pyautogui.press(HomepageKey.WILDERNESS_KEY)

            self.wait_until_image_show(GameTarget.back_to_home)
            time.sleep(Config.CLICK_AFTER_WAIT)

            pyautogui.press(WildnessKey.CLAIM_SHARPODONTY_KEY)
            time.sleep(Config.CLICK_INTERVAL)
            pyautogui.press(WildnessKey.CLAIM_DUST_KEY)
            time.sleep(Config.CLICK_INTERVAL)
            pyautogui.press(WildnessKey.GAIN_CHARACTER_BOND_KEY)
            time.sleep(Config.CLICK_INTERVAL)
            pyautogui.press(GeneralKey.BACK_KEY)

            self.wait_until_image_show(GameTarget.home_hide)
            return True

            # self.wait_and_click(self.wild_button)
            # self.wait_and_click(self.back_to_home_button, timeout=240)
            
            # if self.is_element_visible(self.wild_lichi_info_btn):
            #     self.wait_and_click(self.wild_lichi_info_btn)
            #     self.wait_and_click(self.wild_lichi_collect_btn)
                
            # if self.is_element_visible(self.wild_weichen_info_btn):
            #     self.wait_and_click(self.wild_weichen_info_btn)
            #     self.wait_and_click(self.wild_weichen_collect_btn)

            # if self.is_element_visible(self.friendly_button):
            #     self.wait_and_click(self.friendly_button)

            # self.wait_and_click(self.back_to_home_button)
            # return True


        except Exception as e:
            print(f"荒原收集失败: {str(e)}")
            return False
        

    # # 专属按钮定义
    # wild_button = Button(name='wild_button', path='./assets/wildern.png')
    # wild_lichi_info_btn = Button(name='wild_lichi_info_btn', path='./assets/wild_lichi_info_btn.png')
    # wild_lichi_collect_btn = Button(name='wild_lichi_collect_btn', path='./assets/wild_lichi_collect_btn.png')
    # wild_weichen_info_btn = Button(name='wild_weichen_info_btn', path='./assets/wild_weichen_info_btn.png')
    # wild_weichen_collect_btn = Button(name='wild_weichen_collect_btn', path='./assets/wild_weichen_collect_btn.png')
    # friendly_button = Button(name='friendly_button', path='./assets/friendly_collect_button.jpg')
    # back_to_home_button = Button(name='back_to_home_button', path='./assets/back_to_home_button.png')