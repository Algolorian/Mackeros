import keyboard
import pyautogui
import playsound
import sys


playsound.playsound(r'C:\Program Files\Mackeros\Rapid-120\audio\Start-rapid-120.mp3')


def close():
    playsound.playsound(r'C:\Program Files\Mackeros\Rapid-120\audio\Exit-Binary.mp3', True)
    sys.exit(0)


while True:
    if keyboard.is_pressed('alt'):
        pyautogui.click(clicks=15)
    elif keyboard.is_pressed('esc'):
        close()

# cps = 120
