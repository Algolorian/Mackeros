import os
import shutil
import pyautogui

profile = os.environ['USERPROFILE']
path = os.getcwd()
location = 'C:\\Program Files\\Mackeros\\'


if not os.path.isdir('C:\\Program Files\\Mackeros\\'):
    os.mkdir('C:\\Program Files\\Mackeros\\')

if not os.path.isdir('C:\\Program Files\\Mackeros\\BloonsTD\\'):
    os.mkdir('C:\\Program Files\\Mackeros\\BloonsTD\\')

if not os.path.isdir('C:\\Program Files\\Mackeros\\BloonsTD\\audio\\'):
    os.mkdir('C:\\Program Files\\Mackeros\\BloonsTD\\audio\\')

shutil.move(f'{path}\\ReadMe-1.2.txt', f'{location}BloonsTD\\ReadMe-1.2.txt')
shutil.move(f'{path}\\Mackeros-btd-1.2.exe', f'{profile}\\Desktop\\Mackeros-btd-1.2.exe')
shutil.move(f'{path}\\Start-btd-1.2.mp3', f'{location}BloonsTD\\audio\\Start-btd-1.2.mp3')
shutil.move(f'{path}\\Exit-Binary.mp3', f'{location}BloonsTD\\audio\\Exit-Binary.mp3')

pyautogui.alert(text='Installation complete', title='Install status', button='OK')
