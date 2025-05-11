from collections import deque
import json
from config import TASK_CACHE_FILE

class TaskContainer:
    def __init__(self):
        self.tasks = deque()
        self.load_tasks()

    def add_task(self, task: dict):
        """添加任务到队列末尾"""
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_id: str):
        """根据任务ID移除任务"""
        self.tasks = deque([t for t in self.tasks if t.get('id') != task_id])
        self.save_tasks()

    def get_next_task(self) -> dict:
        """获取并移除队列头部任务"""
        if self.tasks:
            return self.tasks.popleft()
        return None

    def load_tasks(self):
        """从缓存文件加载任务"""
        try:
            with open(TASK_CACHE_FILE, 'r', encoding='utf-8') as f:
                self.tasks = deque(json.load(f))
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = deque()

    def save_tasks(self):
        """保存任务到缓存文件"""
        with open(TASK_CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(list(self.tasks), f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    container = TaskContainer()
    # 示例：添加任务
    container.add_task({"id": "task1", "name": "日常任务"})
    # 示例：获取任务
    print(container.get_next_task())