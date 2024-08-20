import  os  #Demo1_14.py

name = 'reverse_1999'

ui = 'mainwindow' + '.ui'   #被转换的ui文件
target_name = 'reverse_1999_ui.py'
path = r'D:\Qt_Project' + '\\' + name   #ui文件所在路径

os.chdir(path)  #将ui文件所在路径设置成当前路径
cmdTemplate = "PySide6-uic  {ui}  -o  {py}".format(ui=ui,py=target_name)  #文本模板
os.system(cmdTemplate)  #执行转换命令


