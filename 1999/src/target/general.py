from target.target import Target


class GameTarget:
    # used by many tasks
    back_to_home = Target(name = 'back_to_home_target', path = '../assets/back_to_home_target.png')
    home_hide = Target(name = 'home_hide_target', path = '../assets/home_hide_target.png')
    start_action = Target(name = 'start_action_target', path = '../assets/start_action.png')


    # enter_the_show_button = Button('enter_the_show_button', path = './assets/enter_the_show_button.png')


    # used in start game task
    game_title = Target(name = "game_title_btn", path = "../assets/game_title_btn.png")
    return_to_login = Target(name = "return_to_login_target", path = "../assets/return_to_login.png")
    # used in battle

    # used in the poussiere

    # used in pneuma analysis
    resource = Target(name = "resource_target", path = "../assets/resource_target.png")
    psy_free_times = Target(name = "psy_free_times_target", path = "../assets/psy_free_times.png")
    pneuma_analysis = Target(name = "pneuma_analysis_target", path = "../assets/pneuma_analysis.png")
    pneuma_07 = Target(name = "pneuma_07_target", path = "../assets/psy_07.png")
    replay_2_times = Target(name = "replay_2_times_target", path = "../assets/replay_2_times.png")
    replay_4_times = Target(name = "replay_4_times_target", path = "../assets/replay_4_times.png")
    replay_info = Target(name = "replay_info_target", path = "../assets/replay_info.png")
    battle_win = Target(name = "battle_win_target", path = "../assets/battle_win.png")
    
