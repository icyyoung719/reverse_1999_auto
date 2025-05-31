import os
import sys

def list_dir(path, prefix='', is_last=False):
    entries = [e for e in os.listdir(path) if not e.startswith('.')]  # 跳过隐藏文件
    entries = [e for e in entries 
               if not (os.path.isfile(os.path.join(path, e)) 
               and os.path.splitext(e)[1].lower() in ['.pyc', '.png', '.jpg'])]
    entries.sort(key=lambda x: (not os.path.isdir(os.path.join(path, x)), x))  # 目录在前，文件在后
    
    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last_entry = (i == len(entries) - 1)
        
        # 绘制树状连接符
        if is_last:
            connector = '    ' + ('└── ' if is_last_entry else '├── ')
        else:
            connector = '│   ' + ('└── ' if is_last_entry else '├── ')
        
        # 打印当前条目
        print(prefix + connector + entry)
        
        # 递归处理子目录
        if os.path.isdir(full_path):
            new_prefix = prefix + ('    ' if is_last else '│   ')
            list_dir(full_path, new_prefix, is_last_entry)

if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    root_name = os.path.basename(root) if root != '.' else os.path.basename(os.getcwd())
    print(root_name + '/')
    list_dir(root, '', True)