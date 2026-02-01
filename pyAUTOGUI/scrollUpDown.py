import pyautogui
import time

SCROLL_AMOUNT = 300  # positive = scroll up, negative = scroll down
print("Starting scroll up and down...")
while True:
    pyautogui.scroll(SCROLL_AMOUNT)   # scroll up
    time.sleep(1)
    
    pyautogui.scroll(-SCROLL_AMOUNT)  # scroll down
    time.sleep(1)
