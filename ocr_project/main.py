import time
import cv2
import uiautomator2 as u2
from PIL import Image
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from cnocr import CnOcr

# 初始化OCR模型
ocr = CnOcr()

# 设置Tesseract路径（Windows用户需要此行）
# 如果不使用Tesseract，可以将这行删除
# pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'  # 根据你的安装位置调整

# 连接到设备
d = u2.connect()

# 裁剪区域常量
LEFT_REGION = (277, 593, 437, 680)
RIGHT_REGION = (653, 593, 813, 680)

def log_time(label, start_time):
    """打印执行时间的辅助函数"""
    elapsed_time = time.time() - start_time
    print(f"{label} 耗时：{elapsed_time:.4f} 秒")

def get_number_cnocr(image_region):
    """使用CnOcr提取图像中的数字"""
    result = ocr.ocr_for_single_line(np.array(image_region))
    target_num = result["text"]
    return int(target_num) if target_num.isdigit() else None

def process_image(image, region):
    """从图像中提取指定区域的数字"""
    cropped_image = image.crop(region)
    return get_number_cnocr(cropped_image)

def process_images_in_parallel(image):
    """并行处理左右区域的图像"""
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_left = executor.submit(process_image, image, LEFT_REGION)
        future_right = executor.submit(process_image, image, RIGHT_REGION)
        left_number = future_left.result()
        right_number = future_right.result()
    log_time("处理左右图像", start_time)
    return left_number, right_number

def swipe(is_left):
    """执行滑动操作"""
    start_time = time.time()
    swipe_points = {
        True: [(353, 800), (408, 831), (353, 850)],  # 左滑动路径
        False: [(847, 800), (792, 831), (847, 850)]  # 右滑动路径
    }
    d.swipe_points(swipe_points[is_left], duration=0.01)
    log_time("执行滑动", start_time)

def main():
    while True:
        # 截取屏幕图像
        start_time = time.time()
        screenshot_image = d.screenshot(format='pillow')
        log_time("截屏图像", start_time)

        # 获取左右数字
        left_number, right_number = process_images_in_parallel(screenshot_image)

        if left_number is None or right_number is None:
            continue  # 如果识别不到数字则跳过当前循环

        # 比较数字并执行滑动
        start_time = time.time()
        swipe(left_number > right_number)
        log_time("滑动指令处理", start_time)

        # 等待一段时间以避免频繁操作
        time.sleep(0.38)

if __name__ == "__main__":
    main()
