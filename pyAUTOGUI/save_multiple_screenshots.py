import pyautogui
from pynput import keyboard
from datetime import datetime
import os
import time

# CONFIG
SAVE_DIR = r"C:\Users\LENOVO\Python_Projects\screenshots"
HOTKEY = {keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode(char='s')}

os.makedirs(SAVE_DIR, exist_ok=True)

pressed_keys = set()

def take_screenshot():
    time.sleep(0.2)  # small delay to avoid capturing key overlay
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(SAVE_DIR, filename)

    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)

    print(f"Screenshot saved: {filepath}")

def on_press(key):
    pressed_keys.add(key)

    if all(k in pressed_keys for k in HOTKEY):
        take_screenshot()
        pressed_keys.clear()  # prevent repeated triggers

    if key == keyboard.Key.esc:
        print("Program terminated.")
        return False  # stop listener

def on_release(key):
    pressed_keys.discard(key)

print("Press Ctrl + Shift + S to take a screenshot.")
print("Press Esc to exit.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
