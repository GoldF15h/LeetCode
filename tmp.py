import keyboard
import time
import pyautogui

print('RUNNING')
while True :

    if keyboard.is_pressed('q') :
        break
    
    time.sleep(0.01)
    pyautogui.typewrite('aaaaaaaaaa')

print('END')