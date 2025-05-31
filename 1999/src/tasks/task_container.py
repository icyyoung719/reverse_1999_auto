from enum import Enum
import queue
import threading
from typing import Optional, Callable, Any
from .task import Task
import logging

class TaskStatus(Enum):
    """任务状态枚举"""
    PENDING = "pending"      # 等待执行
    RUNNING = "running"      # 正在执行
    COMPLETED = "completed"  # 执行完成
    FAILED = "failed"        # 执行失败

class TaskContainer:
    """
    线程安全的任务容器类，支持动态添加和执行任务
    """
    def __init__(self):
        self._task_queue = queue.PriorityQueue()  # 优先级队列
        self._lock = threading.Lock()  # 线程锁
        self._running = True  # 运行状态标志
        self._current_task: Optional[Task] = None
        self._task_statuses = {}  # 任务状态字典
        self._worker_thread = threading.Thread(target=self._worker, daemon=True)
        self._worker_thread.start()

    def add_task(self, task: Task, priority: int = 0) -> None:
        """
        添加新任务到容器
        :param task: 要添加的任务
        :param priority: 任务优先级，数字越小优先级越高
        """
        with self._lock:
            self._task_queue.put((priority, task))
            self._task_statuses[task] = TaskStatus.PENDING

    def stop(self) -> None:
        """停止任务容器"""
        self._running = False
        if self._worker_thread.is_alive():
            self._worker_thread.join()

    def get_task_status(self, task: Task) -> Optional[TaskStatus]:
        """获取指定任务的状态"""
        return self._task_statuses.get(task)

    def get_current_task(self) -> Optional[Task]:
        """获取当前正在执行的任务"""
        with self._lock:
            return self._current_task

    def _worker(self) -> None:
        """工作线程，负责执行队列中的任务"""
        while self._running:
            try:
                priority, task = self._task_queue.get(timeout=1.0)
                with self._lock:
                    self._current_task = task
                    self._task_statuses[task] = TaskStatus.RUNNING

                try:
                    task.run()
                    with self._lock:
                        self._task_statuses[task] = TaskStatus.COMPLETED
                except Exception as e:
                    logging.error(f"Task execution failed: {str(e)}")
                    with self._lock:
                        self._task_statuses[task] = TaskStatus.FAILED
                finally:
                    with self._lock:
                        self._current_task = None
                    self._task_queue.task_done()

            except queue.Empty:
                continue  # 队列为空时继续等待

    def clear(self) -> None:
        """清空任务队列"""
        with self._lock:
            while not self._task_queue.empty():
                self._task_queue.get()
                self._task_queue.task_done()

    def get_all_task_statuses(self) -> dict:
        """获取所有任务的状态"""
        with self._lock:
            return self._task_statuses.copy()

    def is_empty(self) -> bool:
        """检查任务队列是否为空"""
        return self._task_queue.empty()

    def get_queue_size(self) -> int:
        """获取队列中的任务数量"""
        return self._task_queue.qsize()
