import sys
import os
import ctypes
import time
import logging

from tasks.task_container import TaskContainer, TaskStatus
from tasks.start_game import StartGame, CloseNotice
from tasks.wildness import WildernessCollect
from tasks.pneuma_analysis import PneumaAnalysis
from tasks.the_poussiere import ThePoussiere
from tasks.daily_mission_collect import DailyMissionCollect, DailyRoarJukeboxCollect

from config.config import Config

from ui import MainWindow
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtCore import Slot

def require_admin():
    """检查并请求管理员权限"""
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, os.path.abspath(sys.argv[0]), None, 1)
        sys.exit()

def initialize_tasks(container: TaskContainer):
    """初始化并添加所有任务到容器"""
    # 游戏启动和初始化任务 - 最高优先级
    container.add_task(StartGame(), priority=0)
    container.add_task(CloseNotice(), priority=1)
    
    # 主要游戏任务 - 中等优先级
    container.add_task(WildernessCollect(), priority=2)
    container.add_task(PneumaAnalysis(), priority=3)
    container.add_task(ThePoussiere(), priority=4)
    
    # 可选任务 - 较低优先级
    # container.add_task(DailyMissionCollect(), priority=5)  # 自动发邮件，暂不需要
    container.add_task(DailyRoarJukeboxCollect(), priority=6)

def main():
    """主函数"""
    try:
        setup_logging()
        logging.info("初始化系统...")
        
        container = TaskContainer()
        
        logging.info("等待游戏启动...")
        time.sleep(5)
        
        initialize_tasks(container)
        logging.info(f"已添加 {container.get_queue_size()} 个任务到队列")
        
        while not container.is_empty():
            current_task = container.get_current_task()
            # if current_task:
            #     logging.info(f"正在执行任务: {current_task.__class__.__name__}")
            #     display_task_status(container)
            time.sleep(1)
        
        container.stop()
        logging.info("所有任务已完成")
        
    except Exception as e:
        logging.error(f"执行过程中发生错误: {str(e)}", exc_info=True)
        raise
    finally:
        # input("按回车键退出...") # 防止窗口闪退
        pass

def setup_logging():
    """配置日志系统"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(os.path.join(Config.OUTPUT_DIR, 'log.txt'), encoding='utf-8')
        ]
    )

def display_task_status(container: TaskContainer):
    """显示当前任务状态"""
    statuses = container.get_all_task_statuses()
    if statuses:
        logging.info("当前任务状态:")
        for task, status in statuses.items():
            logging.info(f"- {task.__class__.__name__}: {status.value}")

if __name__ == '__main__':
    # require_admin()  # 如需管理员权限请取消注释
    # main()
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()