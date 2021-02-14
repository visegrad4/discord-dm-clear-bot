import pyautogui
from time import sleep
import os

os.system('mode con: cols=20 lines=20')
sleep(2)

for i in range(100):
    
        sleep(0.1)    
        pyautogui.press('up')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        sleep(0.1)
        pyautogui.press('enter')
        pyautogui.press('enter')
