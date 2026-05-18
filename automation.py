import pyautogui
import time
import threading

# 📸 Screenshot
def take_screenshot():
    pyautogui.screenshot("screenshot.png")
    return "Screenshot taken"

# 🔊 Volume
def volume_up():
    pyautogui.press("volumeup")
    return "Volume increased"

def volume_down():
    pyautogui.press("volumedown")
    return "Volume decreased"

# ⏰ Reminder (NON-BLOCKING ✅)
def set_reminder(seconds, message):
    def reminder():
        time.sleep(seconds)
        print(f"Reminder: {message}")

    threading.Thread(target=reminder).start()
    return "Reminder set"