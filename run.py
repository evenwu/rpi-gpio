#!/usr/bin/python3

from pynput.keyboard import Key, Controller
from gpiozero import Button
from signal import pause
import time

keyboard   = Controller()
btn_up     = Button(  5 )
btn_right  = Button(  6 )
btn_down   = Button( 13 )
btn_left   = Button( 19 )
btn_ok     = Button( 26 )
debounce   = 0.2 

def to_up():
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    print('↑ up')
    time.sleep(debounce)

def to_right():
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    print('→ right')
    time.sleep(debounce)

def to_down():
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    print('↓ down')
    time.sleep(debounce)

def to_left():
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    print('← left')
    time.sleep(debounce)

def push_center():
    start_time = time.time()
    hold_time = 1
    diff = 0

    # 迴圈：如果按著且還沒超過 hold time 就持續計時
    # 跳出迴圈的條件有兩個 1. 放開按鈕 2. 按超過 hold time
    # 最後會取得一個 diff 值
    while (btn_ok.value == 1) and (diff < hold_time) :
        now_time = time.time()
        diff = now_time - start_time

    # 迴圈結束後，依照 diff 值判斷處理
    if diff < hold_time :
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        print('✔ ok')
        time.sleep(debounce)
    else:
        keyboard.press(Key.home)
        keyboard.release(Key.home)
        print('⚑ home')
        time.sleep(.7)

btn_up.when_pressed    = to_up
btn_right.when_pressed = to_right
btn_down.when_pressed  = to_down
btn_left.when_pressed  = to_left
btn_ok.when_pressed    = push_center

pause()
