import cv2
import uiautomator2 as u2
from PIL import Image
import pytesseract
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from cnocr import CnOcr

# 初始化OCR

# 设置 Tesseract 路径（根据你的安装位置调整）
pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'

# 全局变量
left_element = None
right_element = None

# 裁剪数字区域
def get_number_image(target_image, is_left: bool):
    region = (277, 593, 437, 680) if is_left else (653, 593, 813, 680)
    cropped_image = target_image.crop(region)
    return cropped_image

# 设备连接
d = u2.connect()

# 滑动函数
def swipe(is_left: bool):
    if is_left:
        point1, point2, point3 = (353, 800), (408, 831), (353, 850)
    else:
        point1, point2, point3 = (847, 800), (792, 831), (847, 850)

    d.swipe_points([point1, point2, point3], duration=0.01)

# 主循环
while True:
    try:
        # 截屏及元素获取
        if not left_element or not right_element:
            parent_element = d(resourceId="primary-question-wrap")
            left_element = parent_element.child(className="android.widget.TextView", instance=0)
            right_element = parent_element.child(className="android.widget.TextView", instance=1)

        # 提取文本并转换为数字
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_left_text = executor.submit(lambda: int(left_element.get_text()))
            future_right_text = executor.submit(lambda: int(right_element.get_text()))
            left_number = future_left_text.result()
            right_number = future_right_text.result()

        # 比较数字并执行滑动操作
        if left_number > right_number:
            swipe(True)
        else:
            swipe(False)

        time.sleep(0.1)

    except Exception:
        # 重置元素以便在下一次循环时重新获取
        left_element = None
        right_element = None
