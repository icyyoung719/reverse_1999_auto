from PySide6.QtWidgets import (QMainWindow, QWidget, QDockWidget, 
                             QTextEdit, QVBoxLayout, QPushButton, 
                             QMenuBar, QStatusBar, QApplication,
                             QFileDialog, QMessageBox, QLabel,
                             QListWidget, QListWidgetItem)
from PySide6.QtCore import Qt, QSettings
from .managers import LogManager, TaskManager, ConfigManager
from .task_dialog import TaskDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reverse1999 Copilot")
        self.resize(800, 600)
        
        # 初始化管理器
        self.log_manager = LogManager()
        self.task_manager = TaskManager(self.log_manager)
        self.config_manager = ConfigManager()
        
        self.init_ui()
        self.init_connections()
        self.load_settings()
        
    def init_ui(self):
        """初始化UI组件"""
        # 创建中央部件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout(self.central_widget)
        
        # 创建日志输出区域
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.central_layout.addWidget(self.log_output)
        
        # 创建任务控制面板
        self.task_dock = QDockWidget("任务控制", self)
        self.task_widget = QWidget()
        self.task_layout = QVBoxLayout(self.task_widget)
        
        # 任务状态显示
        self.task_status = QLabel("当前无任务运行")
        self.task_layout.addWidget(self.task_status)
        
        # 添加任务列表
        self.task_list_widget = QListWidget()
        self.task_layout.addWidget(QLabel("任务列表"))
        self.task_layout.addWidget(self.task_list_widget)
        
        # 任务控制按钮
        self.start_btn = QPushButton("开始任务")
        self.stop_btn = QPushButton("停止任务")
        self.stop_btn.setEnabled(False)
        
        self.task_layout.addWidget(self.start_btn)
        self.task_layout.addWidget(self.stop_btn)
        
        # 添加任务配置区域
        self.task_layout.addWidget(QLabel("任务配置"))
        # 这里后续可以添加更多任务配置控件
        
        self.task_dock.setWidget(self.task_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.task_dock)
        
        # 创建状态栏
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("就绪")
        
        # 设置菜单栏
        self.create_menus()
        
    def create_menus(self):
        """创建菜单栏"""
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        
        # 文件菜单
        file_menu = self.menu_bar.addMenu("文件")
        file_menu.addAction("加载配置", self.load_config)
        file_menu.addAction("保存配置", self.save_config)
        file_menu.addSeparator()
        file_menu.addAction("退出", self.close)
        
        # 任务菜单
        task_menu = self.menu_bar.addMenu("任务")
        task_menu.addAction("添加任务", self.add_task)
        task_menu.addAction("清除所有任务", self.clear_tasks)
        
        # 配置菜单
        config_menu = self.menu_bar.addMenu("配置")
        config_menu.addAction("设置", self.show_settings)
        
        # 帮助菜单
        help_menu = self.menu_bar.addMenu("帮助")
        help_menu.addAction("关于", self.show_about)
    
    def init_connections(self):
        """初始化信号槽连接"""
        # 连接日志信号
        self.log_manager.new_log.connect(self.update_log)
        
        # 连接任务信号
        self.task_manager.task_started.connect(self.on_task_started)
        self.task_manager.task_stopped.connect(self.on_task_stopped)
        self.task_manager.task_status_changed.connect(self.update_task_status)
        
        # 连接按钮信号
        self.start_btn.clicked.connect(self.on_start)
        self.stop_btn.clicked.connect(self.on_stop)
    
    def load_settings(self):
        """加载应用程序设置"""
        settings = QSettings('Reverse1999', 'Copilot')
        self.restoreGeometry(settings.value('geometry', b''))
        self.restoreState(settings.value('windowState', b''))
        
    def closeEvent(self, event):
        """关闭窗口时保存设置"""
        settings = QSettings('Reverse1999', 'Copilot')
        settings.setValue('geometry', self.saveGeometry())
        settings.setValue('windowState', self.saveState())
        super().closeEvent(event)
    
    def update_log(self, message):
        """更新日志显示"""
        self.log_output.append(message)
    
    def update_task_status(self, status):
        """更新任务状态显示"""
        self.task_status.setText(status)
        self.status_bar.showMessage(status)
    
    def on_task_started(self, task_name):
        """任务开始时的处理"""
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.update_task_status(f"正在执行任务: {task_name}")
    
    def on_task_stopped(self, task_name):
        """任务停止时的处理"""
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.update_task_status("任务已停止")
    
    def on_start(self):
        """开始任务"""
        current_item = self.task_list_widget.currentItem()
        if not current_item:
            QMessageBox.warning(self, "错误", "请先选择要执行的任务")
            return
            
        task_config = current_item.data(Qt.UserRole)
        self.task_manager.start_task(task_config["type"])
    
    def on_stop(self):
        """停止任务"""
        self.task_manager.stop_task()
    
    def load_config(self):
        """加载配置文件"""
        file_name, _ = QFileDialog.getOpenFileName(
            self, "加载配置", "", "JSON文件 (*.json)")
        if file_name:
            self.config_manager.config_file = file_name
            if self.config_manager.load_config():
                self.log_manager.add_log(f"成功加载配置: {file_name}")
            else:
                QMessageBox.warning(self, "错误", "加载配置文件失败")
    
    def save_config(self):
        """保存配置文件"""
        file_name, _ = QFileDialog.getSaveFileName(
            self, "保存配置", "", "JSON文件 (*.json)")
        if file_name:
            self.config_manager.config_file = file_name
            if self.config_manager.save_config():
                self.log_manager.add_log(f"成功保存配置: {file_name}")
            else:
                QMessageBox.warning(self, "错误", "保存配置文件失败")
    
    def add_task(self):
        """添加任务"""
        dialog = TaskDialog(self)
        dialog.task_created.connect(self.on_task_created)
        dialog.exec()
    
    def on_task_created(self, task_config):
        """处理新创建的任务"""
        # 添加到任务管理器
        self.task_manager.add_task(task_config)
        
        # 添加到任务列表显示
        item_text = f"{task_config['type']}"
        if task_config['params']:
            params_text = ", ".join(f"{k}: {v}" for k, v in task_config['params'].items())
            item_text += f" ({params_text})"
        
        item = QListWidgetItem(item_text)
        item.setData(Qt.UserRole, task_config)
        self.task_list_widget.addItem(item)
        
        self.log_manager.add_log(f"添加任务: {item_text}")
    
    def clear_tasks(self):
        """清除所有任务"""
        self.task_manager.task_list.clear()
        self.task_list_widget.clear()
        self.log_manager.add_log("已清除所有任务")
    
    def show_settings(self):
        """显示设置对话框"""
        # 这里后续可以添加设置对话框
        pass
    
    def show_about(self):
        """显示关于对话框"""
        QMessageBox.about(self, "关于",
            "Reverse1999 Copilot\n\n"
            "一个辅助工具，帮助您自动化游戏任务。")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()