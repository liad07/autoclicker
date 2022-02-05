import pyautogui as auto
import keyboard
while True:
    auto.click()
    if keyboard.is_pressed('space'):
        break