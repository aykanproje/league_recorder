import keyboard
import time
from config import RECORD_HOTKEY

def start_recording():
    print("⏺️ Kaydı başlat")
    keyboard.press_and_release(RECORD_HOTKEY)
    time.sleep(1)

def stop_recording():
    print("⏹️ Kaydı durdur")
    keyboard.press_and_release(RECORD_HOTKEY)
    time.sleep(1)
