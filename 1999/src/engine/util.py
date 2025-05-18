import os
import time

def get_current_time() -> str:
    """获取当前时间字符串"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def ensure_dir_exists(dir_path: str):
    """确保目录存在（自动创建）"""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)