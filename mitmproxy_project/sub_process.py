import random
import time
import uiautomator2 as u2

# Global variable to store execution times if needed
execution_times = []

def log_time(label, start_time):
    elapsed_time = time.time() - start_time
    execution_times.append((label, elapsed_time))

d = u2.connect()

def swipe(is_left: bool):
    start_time = time.time()
    if is_left:
        point1 = (353, 800)  # Left-top corner
        point2 = (408, 831)  # Center
        point3 = (353, 850)  # Left-bottom corner
    else:
        point1 = (847, 800)  # Right-top corner
        point2 = (792, 831)  # Center
        point3 = (847, 850)  # Right-bottom corner

    d.swipe_points([point1, point2, point3], duration=0.02)
    log_time("Swipe execution", start_time)

def get_image_click_position():
    # Locate all elements of class 'android.widget.Image'
    elements = d(className="android.widget.Image")

    for element in elements:
        bounds = element.info.get('bounds')

        # Extract the bounds coordinates
        left, top = bounds['left'], bounds['top']
        right, bottom = bounds['right'], bounds['bottom']

        # Check if the bounds fall within the specified range
        if 563 <= left <= 953 and 1302 <= top <= 1480 and 563 <= right <= 953 and 1302 <= bottom <= 1480:
            # Calculate the center of the element for a clickable coordinate
            center_x = (left + right) // 2
            center_y = (top + bottom) // 2
            return center_x, center_y
    return None

def click_location(element):
    bounds = element.bounds()
    center_x = (bounds.left + bounds.right) / 2
    center_y = (bounds.top + bounds.bottom) / 2
    d.click(center_x, center_y)

def encourage():
    image_location = get_image_click_position()
    if image_location:
        for _ in range(random.randint(0, 3)):
            d.click(image_location[0], image_location[1])

def receive_answer(answer_list):
    time.sleep(12)

    for item in answer_list:
        swipe(is_left=(item == ">"))
        time.sleep(0.01 * random.randint(30, 36))

    time.sleep(5)
    # Find the button with the text "开心收下"
    button = d(text="开心收下")

    # Click the button if it exists
    if button.exists:
        button.click()
        time.sleep(3)
        d(text="继续").click()
        time.sleep(3)
        next_element = d(text="继续PK")

        if not next_element.exists:
            d(text="再练一次").click()
        else:
            next_element.click()
