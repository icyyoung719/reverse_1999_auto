from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QLineEdit, 
                             QPushButton, QFormLayout, QSpinBox,
                             QMessageBox)
from PySide6.QtCore import Signal

class TaskDialog(QDialog):
    """任务配置对话框"""
    task_created = Signal(dict)  # 任务创建信号

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("添加任务")
        self.resize(400, 300)
        
        self.task_types = {
            "每日任务收集": {
                "description": "自动收集每日任务奖励",
                "params": {}
            },
            "自动刷关": {
                "description": "重复刷指定关卡",
                "params": {
                    "次数": {"type": "int", "default": 1, "min": 1, "max": 999},
                    "关卡名": {"type": "str", "default": ""}
                }
            },
            "体力消耗": {
                "description": "自动消耗体力直到达到指定值",
                "params": {
                    "目标体力": {"type": "int", "default": 0, "min": 0, "max": 999},
                }
            }
        }
        
        self.init_ui()
        self.init_connections()
        
    def init_ui(self):
        """初始化UI"""
        layout = QVBoxLayout(self)
        
        # 任务类型选择
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("任务类型:"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(self.task_types.keys())
        type_layout.addWidget(self.type_combo)
        layout.addLayout(type_layout)
        
        # 任务描述
        self.description_label = QLabel()
        layout.addWidget(self.description_label)
        
        # 参数配置区域
        self.params_layout = QFormLayout()
        layout.addLayout(self.params_layout)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("确定")
        self.cancel_button = QPushButton("取消")
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        
        # 更新UI显示
        self.update_task_info()
        
    def init_connections(self):
        """初始化信号连接"""
        self.type_combo.currentTextChanged.connect(self.update_task_info)
        self.ok_button.clicked.connect(self.accept_task)
        self.cancel_button.clicked.connect(self.reject)
        
    def update_task_info(self):
        """更新任务信息显示"""
        task_type = self.type_combo.currentText()
        task_info = self.task_types[task_type]
        
        # 更新描述
        self.description_label.setText(task_info["description"])
        
        # 清除原有参数控件
        while self.params_layout.count():
            item = self.params_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # 添加参数控件
        self.param_widgets = {}
        for param_name, param_info in task_info["params"].items():
            if param_info["type"] == "int":
                widget = QSpinBox()
                widget.setMinimum(param_info.get("min", 0))
                widget.setMaximum(param_info.get("max", 999))
                widget.setValue(param_info["default"])
            else:  # str类型
                widget = QLineEdit()
                widget.setText(param_info["default"])
            
            self.param_widgets[param_name] = widget
            self.params_layout.addRow(f"{param_name}:", widget)
    
    def accept_task(self):
        """确认添加任务"""
        task_type = self.type_combo.currentText()
        task_info = self.task_types[task_type]
        
        # 收集参数值
        params = {}
        for param_name, widget in self.param_widgets.items():
            if isinstance(widget, QSpinBox):
                params[param_name] = widget.value()
            else:
                params[param_name] = widget.text()
        
        # 验证参数
        if not self.validate_params(params):
            return
        
        # 创建任务配置
        task_config = {
            "type": task_type,
            "params": params
        }
        
        # 发送任务创建信号
        self.task_created.emit(task_config)
        self.accept()
    
    def validate_params(self, params):
        """验证参数有效性"""
        task_type = self.type_combo.currentText()
        task_info = self.task_types[task_type]
        
        for param_name, param_info in task_info["params"].items():
            value = params[param_name]
            if param_info["type"] == "str" and not value:
                QMessageBox.warning(self, "错误", f"请填写{param_name}")
                return False
        return True
