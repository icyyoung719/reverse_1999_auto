import logging
from logging.handlers import RotatingFileHandler

# 配置日志
logger = logging.getLogger('reverse_1999')
logger.setLevel(logging.DEBUG)

# 文件处理器（轮转日志）
file_handler = RotatingFileHandler('engine/output/log.txt', maxBytes=1024*1024, backupCount=5, encoding='utf-8')
file_handler.setLevel(logging.INFO)

# 控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 格式设置
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)