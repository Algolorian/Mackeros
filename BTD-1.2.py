"""
Author: Timothy Macfarlane
Date: 05/23/21

Purpose: To create keyboard shortcuts on bloons tower defense


pynput doesn't convert to exe use code below' \
Please fall back to 1.6.8 version of pynput. pip install pynput==1.6.8
"""

from pynput import keyboard as key
from time import sleep
from pyautogui import position, click, moveTo, press
import playsound
import pyautogui
import sys
import tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

sell = (720 / 1920 * width, 980 / 1080 * height)
surrender = (956 / 1920 * width, 1036 / 1080 * height)
yes_surrender = (1170 / 1920 * width, 750 / 1080 * height)
power_1 = (876 / 1920 * width, 90 / 1080 * height)
power_2 = (960 / 1920 * width, 140 / 1080 * height)
power_3 = (1056 / 1920 * width, 86 / 1080 * height)
left_tower_4_boost = (420 / 1920 * width, 1045 / 1080 * height)
left_tower_3_boost = (533 / 1920 * width, 1045 / 1080 * height)
left_tower_2_boost = (645 / 1920 * width, 1045 / 1080 * height)
left_tower_1_boost = (758 / 1920 * width, 1045 / 1080 * height)
right_tower_4_boost = (1250 / 1920 * width, 1045 / 1080 * height)
right_tower_3_boost = (1366 / 1920 * width, 1045 / 1080 * height)
right_tower_2_boost = (1479 / 1920 * width, 1045 / 1080 * height)
right_tower_1_boost = (1590 / 1920 * width, 1045 / 1080 * height)
upgrade_left = (1293 / 1920 * width, 990 / 1080 * height)
upgrade_right = (1588 / 1920 * width, 990 / 1080 * height)
target = (733 / 1920 * width, 1035 / 1080 * height)

playsound.playsound(r'C:\Program Files\Mackeros\BloonsTD\audio\Start-btd-1.2.mp3')


def close_hotkeys():
    playsound.playsound(r'C:\Program Files\Mackeros\BloonsTD\audio\Exit-Binary.mp3', True)
    sys.exit(0)


def get_mouse():
    global mouse_pos
    mouse_pos = position()


def clicker():
    pyautogui.click(clicks=20)


def replace_mouse():
    global mouse_pos
    moveTo(mouse_pos)


def choose_target():
    global mouse_pos
    get_mouse()
    click(mouse_pos)
    sleep(0.1)
    click(target)
    replace_mouse()


def sell_tower():
    press('backspace')


def quit_game():
    global mouse_pos
    get_mouse()
    click(surrender)
    click(yes_surrender)
    replace_mouse()


def left_upgrade():
    press(',')


def right_upgrade():
    press('.')


def click_power_1():
    global mouse_pos
    get_mouse()
    click(power_1)
    replace_mouse()


def click_power_2():
    global mouse_pos
    get_mouse()
    click(power_2)
    replace_mouse()


def click_power_3():
    global mouse_pos
    get_mouse()
    click(power_3)
    replace_mouse()


with key.GlobalHotKeys({

    '<esc>': close_hotkeys,

    '<shift>': quit_game,
    '<space>': sell_tower,

    'r': left_upgrade,
    'f': right_upgrade,

    '<alt>': clicker,

    'q': click_power_1,
    'w': click_power_2,
    'e': click_power_3,

    't': choose_target

}) as h:
    h.join()
