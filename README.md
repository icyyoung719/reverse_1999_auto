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
- [ ] OCR识别体力
- [ ] 将输出日志输出到一个对话框之中


## 如何使用
pip 库
```shell
pip install opencv-python pyautogui numpy
```

进入游戏首页（箱子页面）

接下来直接运行 `main.py` 即可。
***

reverse 1999 auto by OCR

## TODO list:
- 重构代码，以回调函数实现
- 将参数（如time.sleep的大小）存放在单独的py文件中调用，提升可读性
- 将截图放在不同的文件夹下，防止每次花费大量时间查找
- 将功能需求存放在容器中，提供运行时添加/删除 功能的效果

我制作了一个游戏脚本，但是这个游戏脚本只能线性运行
我的想法：任务选项间首先平等，将选择的任务添加到某个容器中，每次从中取出任务，完成后检查容器；任务执行过程中能够添加/删除容器中的其他任务；


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
    ├── TODO.md
    ├── function.py
    ├── main.py
    ├── out.txt
    ├── run_1999.bat
    ├── struct.txt
    ├── tree.py
    └── ui_to_py.py
```