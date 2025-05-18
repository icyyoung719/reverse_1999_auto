# from .config import
# from engine.api import BaseAPI
# import json
# import time

# class GameAPI(BaseAPI):
#     def __init__(self):
#         self.task_queue = []
#         self.current_task = None
        
#     def validate_operation(self, func):
#         def wrapper(*args, **kwargs):
#             if not self.check_game_status():
#                 self.auto_recover()
#                 raise RuntimeError("游戏状态异常，已尝试自动恢复")
#             result = func(*args, **kwargs)
#             if not self.verify_operation_result(func.__name__):
#                 raise RuntimeError(f"{func.__name__} 操作验证失败")
#             return result
#         return wrapper

#     def verify_operation_result(self, operation_type):
#         # 操作结果验证逻辑
#         time.sleep(1)
#         return self.screenshot().match_template(f'{operation_type}_success.jpg')

#     def check_game_status(self):
#         # 状态检测核心逻辑
#         try:
#             if not self.screenshot().match_template('home_hide_btn.jpg'):
#                 self.recover_home_state()
#                 return False
#             return True
#         except Exception as e:
#             self.log_error(f"状态检测失败: {str(e)}")
#             return False

#     def load_tasks(self):
#         try:
#             with open(TASK_CACHE_FILE, 'r') as f:
#                 cached = json.load(f)
#                 self.task_queue = [t for t in cached if t['status'] != 'completed']
#                 self._migrate_old_tasks(cached)
#         except (FileNotFoundError, json.JSONDecodeError):
#             self.task_queue = []

#     def save_tasks(self):
#         try:
#             with open(TASK_CACHE_FILE, 'w') as f:
#                 json.dump({
#                     'version': 1.2,
#                     'tasks': [{
#                         'id': t['id'],
#                         'name': t['name'],
#                         'status': t.get('status', 'pending'),
#                         'last_executed': t.get('last_executed'),
#                         'retry_count': t.get('retry_count', 0)
#                     } for t in self.task_queue]
#                 }, f, indent=2)
#         except (IOError, PermissionError) as e:
#             self.log_error(f"任务保存失败: {str(e)}")
#             raise

#     def auto_save(self):
#         if any(t['status'] == 'executing' for t in self.task_queue):
#             self.save_tasks()

#     @validate_operation
#     def add_task(self, task):
#         task['status'] = 'pending'
#         task['retry_count'] = 0
#         self.task_queue.append(task)
#         self.auto_save()

#     @validate_operation
#     def execute_tasks(self):
#         while self.task_queue:
#             task = self.task_queue.pop(0)
#             try:
#                 self.current_task = task
#                 task['status'] = 'executing'
#                 self.auto_save()
                
#                 # 执行具体任务逻辑
#                 getattr(self, f'execute_{task["type"]}')(task)
                
#                 task['status'] = 'completed'
#                 task['last_executed'] = time.strftime('%Y-%m-%d %H:%M:%S')
#             except Exception as e:
#                 task['status'] = 'failed'
#                 task['error'] = str(e)
#                 task['retry_count'] = task.get('retry_count', 0) + 1
#                 if task['retry_count'] < 3:
#                     self.task_queue.append(task)
#                 self.log_error(f"任务执行失败: {task['name']} - {str(e)}")
#             finally:
#                 self.current_task = None
#                 self.auto_save()

#     def remove_task(self, task_id):
#         self.task_queue = [t for t in self.task_queue if t['id'] != task_id]
#         self.auto_save()