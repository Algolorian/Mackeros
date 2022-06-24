import os
import shutil
import pyautogui

profile = os.environ['USERPROFILE']
path = os.getcwd()
location = 'C:\\Program Files\\Mackeros\\'


if not os.path.isdir('C:\\Program Files\\Mackeros\\'):
    os.mkdir('C:\\Program Files\\Mackeros\\')

if not os.path.isdir('C:\\Program Files\\Mackeros\\Rapid-120\\'):
    os.mkdir('C:\\Program Files\\Mackeros\\Rapid-120\\')

if not os.path.isdir('C:\\Program Files\\Mackeros\\Rapid-120\\audio\\'):
    os.mkdir('C:\\Program Files\\Mackeros\\Rapid-120\\audio\\')

shutil.move(f'{path}\\ReadMe.txt', f'{location}Rapid-120\\ReadMe.txt')
shutil.move(f'{path}\\Rapid-Click-120.exe', f'{profile}\\Desktop\\Rapid-Click-120.exe')
shutil.move(f'{path}\\Start-Rapid-120.mp3', f'{location}Rapid-120\\audio\\Start-Rapid-120.mp3')
shutil.move(f'{path}\\Exit-Binary.mp3', f'{location}Rapid-120\\audio\\Exit-Binary.mp3')

pyautogui.alert(text='Installation complete', title='Install status', button='OK')
