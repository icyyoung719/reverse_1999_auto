## 此代码从 [reverse_1999_copilot](https://github.com/BrackRat/reverse_1999_copilot.git) fork并修改。


# 1999 图像识别自动化日常

已实现:
- [x] 荒原收集（微尘+利齿+好感度）
- [x] 意志解析
- [x] 微尘 4 次 100 体力
- [x] 每日任务收集
- [x] 完善自动进入游戏功能
- [x] 利用pyside6，实现GUI程序
- [x] 通过简单的勾选自定义日常行为方案
- [x] 自动缓存设置，不用每次都手动勾选功能

大饼:

[查看 TODO 事项](TODO.md)


## 如何使用
1. pip 库安装依赖
```bash
pip install -r requirements.txt
```
2. 修改`run_1999.bat`中的文件路径为实际的路径，并设置适当的python环境启动方式
3. 双击`run_1999.bat`即可自动以管理员身份运行程序


## 代码结构
```
reverse_1999_copilot/
    ├── 1999
    │   ├── assets
    │   │   └── en
    │   │       └── new
    │   ├── output
    │   │   ├── config.json
    │   │   └── log.txt
    │   └── src
    │       ├── __pycache__
    │       ├── config
    │       │   ├── __pycache__
    │       │   ├── key
    │       │   │   ├── __pycache__
    │       │   │   ├── __init__.py
    │       │   │   ├── general.py
    │       │   │   ├── homepage.py
    │       │   │   └── wildness.py
    │       │   ├── __init__.py
    │       │   └── config.py
    │       ├── engine
    │       │   ├── __pycache__
    │       │   ├── __init__.py
    │       │   ├── api.py
    │       │   ├── engineconfig.py
    │       │   ├── log.py
    │       │   ├── target.py
    │       │   └── util.py
    │       ├── target
    │       │   ├── __pycache__
    │       │   ├── __init__.py
    │       │   ├── general.py
    │       │   └── target.py
    │       ├── tasks
    │       │   ├── __pycache__
    │       │   ├── __init__.py
    │       │   ├── daily_mission_collect.py
    │       │   ├── pneuma_analysis.py
    │       │   ├── start_game.py
    │       │   ├── task.py
    │       │   ├── the_poussiere.py
    │       │   └── wildness.py
    │       ├── ui
    │       │   └── ui.py
    │       ├── __init__.py
    │       ├── api.py
    │       ├── log.py
    │       ├── main.py
    │       └── util.py
    ├── __pycache__
    ├── README.md
    ├── requirements.txt
    ├── TODO.md
    ├── function.py
    ├── main.py
    ├── out.txt
    ├── run_1999.bat
    ├── struct.txt
    ├── tree.py
    └── ui_to_py.py
```