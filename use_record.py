from ast import If
import pyautogui, sys
from pynput.keyboard import Key, Listener
import time


start_time=time.time()

path=input('錄製的檔案名是:')

moves=[]

f = open(path,'r')
pyautogui.PAUSE = 0.002
for row in f.readlines():
    moves.append(row.split(' '))
# print(moves)

now_move=0

flag=[True]

def on_press(key):
    if key == Key.esc:
        flag[0]=False
        return False

with Listener(on_press=on_press
) as listener:

    while(now_move<=len(moves)-1 and flag[0]):
        now_time=time.time()-start_time
        # print(now_time,moves[now_move][4])
        if now_time>=float(moves[now_move][4]):
            move=moves[now_move][0]
            detail=moves[now_move][1]
            x=int(moves[now_move][2])
            y=int(moves[now_move][3])
            # print(x,y)
            if move=='click':
                if detail=='press':
                    print('mousedown')
                    pyautogui.moveTo(x, y)
                    pyautogui.mouseDown()
                else:
                    print('mouseup')
                    pyautogui.moveTo(x, y)
                    pyautogui.mouseUp()
            elif move=='move':
                pyautogui.moveTo(x, y,duration=0.01)
            now_move+=1
            # print('現在跑的')
            # print(now_move,len(moves)-1)
            # print(flag)
    now_time=time.time()-start_time
    # print(now_time,moves[now_move-1][4])
    print('結束腳本')
    listener.stop()
    listener.join()