# 游戏相关配置

class Config:
    # 静态属性（类属性）
    # OCR_WAIT_TIME = 2
    MAX_WAIT_TIME = 10
    CLICK_INTERVAL = 0.5
    # 循环等待到出现所需界面后，等待多久后点击
    CLICK_AFTER_WAIT = 1.5
    GAMETITLE_WAIT_TIME = 5
    TASK_CACHE_FILE = "1999/output/config.json"
    MIN_SIMILARITY = 0.8
    LANGUAGE = "en"
    OUTPUT_DIR = "../output"
    # 游戏分辨率
    GAME_RESOLUTION = (1920, 1080)
    IMG_BASE_RESOLUTION = (1600, 900)
    SCALE = (GAME_RESOLUTION[0] / IMG_BASE_RESOLUTION[0], GAME_RESOLUTION[1] / IMG_BASE_RESOLUTION[1])

    @staticmethod
    def get(key: str, default=None):
        """动态获取配置项"""
        return getattr(Config, key, default)

    @staticmethod
    def set(key: str, value):
        """动态设置配置项"""
        setattr(Config, key, value)