import pyautogui
import time

time.sleep(2)  # Give user 2 seconds to switch to the desired window

while True:
    pyautogui.hotkey('tab')  # Example hotkey combination
    time.sleep(1)  # Wait for a second before the next hotkey press

#                   abc    defghi  jklmn   opqrst   uvwxyz    ABCDEF   GHIJKLMNO  PQRSTUVWXY    Z012   3456789!@#$     %^&*()_+-=[]{}|;:'",.<>?/`~