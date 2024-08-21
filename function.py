import time
import subprocess

from utils import click_on_image, wait_until_image_show, detect_image, scroll_down

language = 'en'


class Button:
    name = None
    path = None
    offset = None
    min_similar = 0.8

    def __init__(self, name, path, min_similar = 0.8, offset = None):
        self.name = name
        if (language == 'en'):
            self.path = path.replace('./assets', './assets/en').replace('jpg', 'png')
        else:
            self.path = path
        self.min_similar = min_similar
        self.offset = offset

    def click(self, similar = 0.8):
        print(f"{self.name} clicked")
        return click_on_image(self.path, similar = similar, click_offset = self.offset)


wild_button = Button(name = 'wild_button', path = './assets/wildern.png')
friendly_button = Button(name = 'friendly_button', path = './assets/friendly_collect_button.jpg')
back_to_home_button = Button(name = 'back_to_home_button', path = './assets/back_to_home_button.png')
wild_lichi_info_btn = Button(name = 'wild_lichi_info_btn', path = './assets/wild_lichi_info.jpg')
wild_lichi_collect_btn = Button(name = 'wild_lichi_collect_btn', path = './assets/wild_lichi_collect_button.jpg')
wild_weichen_info_btn = Button(name = 'wild_weichen_info_btn', path = './assets/wild_weichen_info.jpg')
wild_weichen_collect_btn = Button(name = 'wild_weichen_collect_btn', path = './assets/wild_weichen_btn.jpg')


# 荒原收集
def wilderness_collect():
    wait_until_image_show(home_hide_btn.path)
    wild_button.click()

    wait_until_image_show(back_to_home_button.path)
    time.sleep(1)

    #可以收舍利子
    if detect_image(wild_lichi_info_btn.path):
        wild_lichi_info_btn.click()
        time.sleep(2)
        wild_lichi_collect_btn.click(0.4)
        time.sleep(2)
    #可以微尘
    if detect_image(wild_weichen_info_btn.path):
        wild_weichen_info_btn.click()
        time.sleep(2)
        wild_weichen_collect_btn.click(0.4)
        time.sleep(2)

    if detect_image(friendly_button.path):
        # 可以收好感度
        friendly_button.click()
        time.sleep(3)

    time.sleep(2)

    back_to_home_button.click(0.8)

    wait_until_image_show(home_hide_btn.path)
    return 0


enter_the_show_button = Button('enter_the_show_button', path = './assets/enter_the_show_button.png')
resource_button = Button('resource_button', path = './assets/resource_button.jpg')
the_poussiere_button = Button('the_poussiere_button', path = './assets/the_poussiere_button.jpg')
resource_06_button = Button('resource_06_button', path = './assets/resource_06_button.jpg')
start_action_button = Button('start_action_button', path = './assets/start_action_button.jpg')
replay_4_button = Button('replay_4_button', path = './assets/replay_4_button.jpg', min_similar = 0.9)
switch_replay_button = Button('switch_replay_button', path = './assets/switch_replay_button.jpg')
replay_times_button = Button('replay_times_button', path = './assets/replay_times_button.jpg')
replay_4_switch_button = Button('replay_4_switch_button', path = './assets/replay_4_switch_button.jpg')
replay_4_times_button = Button('replay_4_times_button', path = './assets/replay_4_times_button.jpg')
warning_button = Button('warning_button', path = './assets/warning_button.jpg')


# 尘埃运动 复现4 100体力
def the_poussiere():
    wait_until_image_show(home_hide_btn.path)
    enter_the_show_button.click()
    wait_until_image_show(resource_button.path)
    time.sleep(0.5)

    resource_button.click()

    wait_until_image_show(the_poussiere_button.path)
    time.sleep(1)
    the_poussiere_button.click()

    wait_until_image_show(resource_06_button.path)
    time.sleep(0.5)
    resource_06_button.click()

    wait_until_image_show(start_action_button.path)
    time.sleep(1)
    start_action_button.click()
    wait_until_image_show(warning_button.path)

    if detect_image(replay_4_button.path, similar = 0.95):
        # 如果是4等复现，直接复现
        replay_4_times_button.click()
    else:
        # 如果是 Action 先切换到复现
        if detect_image(start_action_button.path):
            switch_replay_button.click()
        time.sleep(1)
        replay_times_button.click()
        time.sleep(1)
        replay_4_switch_button.click()

    time.sleep(1)
    replay_4_times_button.click()

    wait_until_image_show(replaying_info.path)
    if detect_image(replaying_info.path):
        print("正在回放中...")

    wait_until_image_show(battle_win_info.path, timeout = 240)
    time.sleep(5)
    battle_win_info.click()

    wait_until_image_show(back_to_home_button.path)
    back_to_home_button.click()

    wait_until_image_show(home_hide_btn.path)
    return 0


psy_free_text = Button("psy_free_text", "./assets/psy_free_times.png", offset = [0, -150])
psy_07_btn = Button("psy07btn", "./assets/psy_07_button.jpg")
replay_2_button = Button("replay_2_button", "./assets/replay_2_button.png")
replay_2_switch_button = Button("replay_2_switch_button", "./assets/replay_2_switch_button.jpg")
replay_2_times_button = Button("replay_2_times_button", "./assets/replay_2_times_button.jpg")
replaying_info = Button("replaying_info", "./assets/replaying_info.jpg")
battle_win_info = Button("battle_win_info", "./assets/battle_win_info.jpg")
home_hide_btn = Button("home_hide_btn", "./assets/home_hide_btn.jpg")


# 免费意志解析 2 次
def daily_battle_psy():
    wait_until_image_show(home_hide_btn.path)
    enter_the_show_button.click()
    wait_until_image_show(resource_button.path)
    time.sleep(0.5)

    resource_button.click()

    wait_until_image_show(psy_free_text.path)
    psy_free_text.click()

    wait_until_image_show(psy_07_btn.path)
    time.sleep(0.3)
    psy_07_btn.click()
    time.sleep(0.5)

    wait_until_image_show(start_action_button.path)
    start_action_button.click()

    wait_until_image_show(warning_button.path)

    if detect_image(replay_2_button.path, similar = 0.95):
        # 如果是2等复现，直接复现
        replay_2_times_button.click()
    else:
        # 如果是 Action 先切换到复现
        if detect_image(start_action_button.path):
            switch_replay_button.click()
        time.sleep(1)
        replay_times_button.click()
        time.sleep(1)
        replay_2_switch_button.click()

    replay_2_times_button.click()

    wait_until_image_show(replaying_info.path)
    if detect_image(replaying_info.path):
        print("正在回放中...")

    wait_until_image_show(battle_win_info.path, timeout = 240)
    time.sleep(5)
    battle_win_info.click()

    wait_until_image_show(back_to_home_button.path)
    back_to_home_button.click()

    wait_until_image_show(home_hide_btn.path)
    return 0


daily_task_btn = Button("daily_task_btn", "./assets/daily_task_btn.jpg")
claim_all_btn = Button("claim_all_btn", "./assets/claim_all_btn.jpg")
get_item_info = Button("get_item_info", "./assets/get_item_info.jpg")


# 每日任务收集
def daily_task_claim():
    if detect_image(home_hide_btn.path) is False:
        return "不在箱子里!"

    wait_until_image_show(daily_task_btn.path)
    time.sleep(0.5)
    daily_task_btn.click()

    time.sleep(2)
    if detect_image(claim_all_btn.path):
        claim_all_btn.click()
        time.sleep(2)

        # 如果领取到了东西
        wait_until_image_show(get_item_info.path)
        time.sleep(1)
        get_item_info.click()
        time.sleep(1)

        wait_until_image_show(back_to_home_button.path)
        back_to_home_button.click()

        wait_until_image_show(home_hide_btn.path)
    else:
        wait_until_image_show(back_to_home_button.path)
        back_to_home_button.click()

        wait_until_image_show(home_hide_btn.path)
    return True


windows_btn = Button("windows_btn", "./assets/windows_btn.png")
search_column_btn = Button("search_column", "./assets/search_column_btn.png")
start_reverse_1999_btn = Button("start_reverse_1999_btn", "./assets/start_reverse_1999_btn.png")
play_game_btn = Button("play_game_btn", "./assets/play_game_btn.png")
game_title_btn = Button("game_title_btn", "./assets/game_title_btn.png")
game_path = r'D:\1999\reverse1999_global\reverse1999-launcher.exe'


def OCR_start_game():
    windows_btn.click()
    time.sleep(1.5)

    scroll_down(search_column_btn.path, 0.7, [0, 300])
    time.sleep(0.5)

    start_reverse_1999_btn.click()

    wait_until_image_show(play_game_btn.path)
    play_game_btn.click()

    wait_until_image_show(game_title_btn.path)
    time.sleep(7)

    game_title_btn.click()


def path_start_game(path = game_path):
    subprocess.Popen(path)

    wait_until_image_show(play_game_btn.path)
    play_game_btn.click()

    wait_until_image_show(game_title_btn.path)
    time.sleep(7)

    game_title_btn.click()


reverse_1999_btn = Button("reverse_1999_btn", "./assets/reverse_1999.png")


def find_game():
    reverse_1999_btn.click()


if __name__ == "__main__":
    # 等待 1 秒后开始
    time.sleep(1)

    # 开始游戏
    # OCR_start_game()
    # path_start_game()
    #
    # # 荒原
    wilderness_collect()
    # #
    # # 意志解析 2 次
    # daily_battle_psy()
    # #
    # # 微尘 4 次 100 体力
    # the_poussiere()
    # #
    # # 每日任务收集
    # daily_task_claim()
