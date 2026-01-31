import pyautogui
import time

IMAGE_PATH = r"C:\Users\LENOVO\Python_Projects\pyAUTOGUI\pyautogui\Copilot.png"
CHECK_INTERVAL = 0.5

print("Waiting for image to appear on screen...")

while True:
    try:
        location = pyautogui.locateOnScreen(IMAGE_PATH, confidence=0.8)
        print("Image detected at:", location)
        print(time.strftime("%H:%M:%S"))

        break

    except pyautogui.ImageNotFoundException:
        # Image not found yet → keep waiting
        time.sleep(CHECK_INTERVAL)

print("Program terminated after detecting the image.")
