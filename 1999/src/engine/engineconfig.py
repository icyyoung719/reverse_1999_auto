# engine的配置，如果游戏自己也有config.py，会覆盖这里的配置

class EngineConfig:
    # 静态属性（类属性）
    PRESS_WAIT_TIME = 0.5  # 按键后等待的响应时间（秒）
    WAIT_INTERVAL = 0.5  # 等待间隔时间（秒）
    MAX_WAIT_TIME = 10  # 最长等待时间（秒）
    MIN_SIMILARITY = 0.8

    @staticmethod
    def get(key: str, default=None):
        """动态获取配置项"""
        return getattr(EngineConfig, key, default)

    @staticmethod
    def set(key: str, value):
        """动态设置配置项"""
        setattr(EngineConfig, key, value)