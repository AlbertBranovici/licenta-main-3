import time
import pyautogui

def auto_type(username, password):
    # Switch to the target application (e.g., a text editor or browser)
    time.sleep(3)  # Add a delay to switch to the correct window

    # Simulate typing the username
    pyautogui.typewrite(username)
    pyautogui.press('tab')  # Move to the password field
    pyautogui.typewrite(password)

