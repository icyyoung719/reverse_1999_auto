当前项目计划：
1. 重新调整项目结构，将代码拆分重构，具体计划如下：
    1. 将游戏无关的部分拆分到engine目录下，并且engine目录下添加api.py文件，用于提供自动化的API接口，如OCR
    2. 将游戏相关的部分拆分到单独目录下，对于1999，也提供util,aapi等
结构设计如下：
```
project/
├── engine
│   ├── api.py
│   ├── util.py
│   ├── config.py
│   ├── log.py：待实现
│   └── other1.py
│   └── other2.py
│   └── .....
├── 1999
│   ├── util.py
│   ├── api.py
│   ├── config.py :存放配置信息，如OCR后等待时间、最长等待时间
|   ├── tasks
│   │   ├── basetask.py
│   │   ├── task1.py
│   │   ├── task2.py
│   │   └──...
│   ├── assets
│   │   ├── img1.png：OCR图片
│   │   └── img2.png：OCR图片
│   |   └── ...
│   ├── main.py
│   └── ui.py:存放pyside6的ui文件
│   └── ......
|   └── output：
│   │   ├── log.txt：日志文件，用于调试（有待实现，暂时搁置）
│   │   └── config.json：实时生成的配置文件，保留上一次执行时的任务，缓存方便下一次操作
└── ui_to_py.py:用于将ui文件转换为py文件
|── README.md
└── TODO.md
```

2. 游戏脚本只能线性运行，我们可以将功能需求存放在容器(也许是队列？)中，提供运行时添加/删除 功能的效果



搞清楚wait_until_image_show等方法要谁提供！




## 问题
1. 荒原，好像是ESC后要等一会
2. Psy有待后续测试
3. 




