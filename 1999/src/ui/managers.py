from PySide6.QtCore import QObject, Signal
import json
import os

class LogManager(QObject):
    """日志管理器"""
    new_log = Signal(str)  # 新日志信号

    def __init__(self):
        super().__init__()
        self.logs = []

    def add_log(self, message):
        """添加新日志"""
        self.logs.append(message)
        self.new_log.emit(message)

class TaskManager(QObject):
    """任务管理器"""
    task_started = Signal(str)  # 任务开始信号
    task_stopped = Signal(str)  # 任务停止信号
    task_status_changed = Signal(str)  # 任务状态改变信号

    def __init__(self, log_manager):
        super().__init__()
        self.log_manager = log_manager
        self.current_task = None
        self.task_list = []

    def add_task(self, task):
        """添加任务"""
        self.task_list.append(task)
        self.log_manager.add_log(f"添加任务: {task}")

    def start_task(self, task_name):
        """开始任务"""
        self.current_task = task_name
        self.task_started.emit(task_name)
        self.log_manager.add_log(f"开始任务: {task_name}")

    def stop_task(self):
        """停止任务"""
        if self.current_task:
            self.task_stopped.emit(self.current_task)
            self.log_manager.add_log(f"停止任务: {self.current_task}")
            self.current_task = None

class ConfigManager(QObject):
    """配置管理器"""
    config_changed = Signal(dict)  # 配置改变信号

    def __init__(self):
        super().__init__()
        self.config = {}
        self.config_file = "config.json"

    def load_config(self):
        """加载配置"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
                    self.config_changed.emit(self.config)
                return True
            except Exception as e:
                print(f"加载配置失败: {e}")
        return False

    def save_config(self):
        """保存配置"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"保存配置失败: {e}")
            return False

    def update_config(self, key, value):
        """更新配置"""
        self.config[key] = value
        self.config_changed.emit(self.config)
        self.save_config()
