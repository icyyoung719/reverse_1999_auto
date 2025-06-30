import mss
import pyautogui
import numpy as np
import cv2
import time
import json
from screeninfo import get_monitors  # 获取显示器信息


def capture_screen_region(left, top, width, height):
    """ 使用 mss 截取指定区域，更好支持多屏和全屏游戏 """
    with mss.mss() as sct:
        monitor = {"left": int(left), "top": int(top), "width": int(width), "height": int(height)}
        img = sct.grab(monitor)
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # mss返回的是BGRA
    return frame

def resize_template(template, scale):
    scale_x, scale_y = scale
    new_size = (int(template.shape[1] * scale_x), int(template.shape[0] * scale_y))
    return cv2.resize(template, new_size, interpolation=cv2.INTER_LINEAR)

def find_template(template, screenshot):
    """使用 OpenCV 模板匹配"""
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_val, max_loc


def find_image_on_all_monitors(template, scale, similar=0.8):
    """
    在所有显示器上查找图像
    返回值: (center_x, center_y) 或 False
    """
    template = resize_template(template, scale)
    for monitor in get_monitors():
        try:
            # 截图当前显示器区域
            screenshot = capture_screen_region(
                left=monitor.x,
                top=monitor.y,
                width=monitor.width,
                height=monitor.height
            )
            max_val, max_loc = find_template(template, screenshot)

            if max_val >= similar:
                template_h, template_w, _ = template.shape
                center_x = monitor.x + max_loc[0] + template_w // 2
                center_y = monitor.y + max_loc[1] + template_h // 2
                return center_x, center_y
        except Exception as e:
            print(f"在屏幕 {monitor} 上处理时出错: {e}")
    return False


def click_on_image(template_path, scale, similar=0.8, click_offset=None):
    if click_offset is None:
        click_offset = [0, 0]
    template = cv2.imread(template_path)
    if template is None:
        print(f"无法加载图像: {template_path}")
        return False

    location = find_image_on_all_monitors(template, scale, similar=similar)
    if location:
        center_x, center_y = location
        center_x += click_offset[0]
        center_y += click_offset[1]
        pyautogui.click(center_x, center_y)
        print(f"Clicked on {template_path} at ({center_x}, {center_y})")
        return center_x, center_y
    else:
        print("Image not found on the screen.")
        return False


def wait_until_image_show(template_path, scale, similar=0.8, timeout=40, interval=1):
    start_time = time.time()
    template = cv2.imread(template_path)
    if template is None:
        print(f"无法加载图像: {template_path}")
        return False

    while time.time() - start_time < timeout:
        location = find_image_on_all_monitors(template, scale, similar=similar)
        if location:
            center_x, center_y = location
            print(f"Image found at ({center_x}, {center_y})")
            return center_x, center_y
        print(f"waiting----- {template_path}")
        time.sleep(interval)
    print(f"Image not found within {timeout} seconds.")
    return False


def detect_image(template_path, scale, similar=0.8):
    template = cv2.imread(template_path)
    if template is None:
        print(f"无法加载图像: {template_path}")
        return False

    location = find_image_on_all_monitors(template, scale, similar=similar)
    return bool(location)


def scroll_down(template_path,similar=0.8, click_offset = None ):
    # if not wait_until_image_show(template_path):
    #     print(f"Image not found within 30 seconds.")
    #     return False
    center_x, center_y = wait_until_image_show(template_path, similar)
    center_x = click_offset[0] + center_x
    center_y = click_offset[1] + center_y
    pyautogui.moveTo(center_x, center_y)
    pyautogui.scroll(-1)
    return True


def save_json(config_data):
    with open('config.json', 'w') as f:
        # 使用dump函数将配置数据写入文件
        json.dump(config_data, f, indent = 4)  # indent=4 使输出更美观，不是必需的


def load_json():
    try:
        with open('config.json', 'r') as f:
            config_data = json.load(f)
        return config_data
    except FileNotFoundError:
        print("欢迎初次使用")
    except json.JSONDecodeError:
        print("配置文件config.json格式错误，无法解析。")
    except Exception as e:
        print(f"读取配置文件时发生错误：{e}")
    return None