import pyautogui
import time

previous_position = pyautogui.position()

while True:
    time.sleep(0.5)
    current_position = pyautogui.position()

    if current_position != previous_position:
        print(current_position)
        previous_position = current_position
