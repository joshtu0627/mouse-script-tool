import pyautogui, sys
from pynput.mouse import Listener,Button
import time
# from pynput.keyboard import Key, Listener

path=input('請輸入你想要輸出的腳本名:')

f=open(path, 'w')

start_time= time.time()


click_start=[0,0]
clicked=[False]

def on_move(x, y):
    now_time=time.time()-start_time
    # print(clicked[0])
    if clicked[0]==True:
        f.write('move . '+str(x)+' '+str(y)+' '+str(now_time)+' \n')
        print(f"鼠標移動到: ({x}, {y})")


def on_click(x, y, button, is_press):
    now_time=time.time()-start_time
    if button == Button.right:
        f.close()
        return False
    if is_press:
        clicked[0]=True
        # print(clicked)
        click_start[0]=x
        click_start[1]=y
        f.write('click press '+str(x)+' '+str(y)+' '+str(now_time)+' \n')
        
    else:
        clicked[0]=False
        f.write('click unpress '+str(x)+' '+str(y)+' '+str(now_time)+' \n')
    print(f"鼠標{button}鍵在({x}, {y})處{'按下' if is_press else '松開'}")


def on_scroll(x, y, dx, dy):
    if dx:
        print(f"滑輪在({x}, {y})處向{'右' if dx > 0 else '左'}滑")
    else:
        print(f"滑輪在({x}, {y})處向{'下' if dy > 0 else '上'}滑")


with Listener(
   on_move=on_move,
   on_click=on_click,
   on_scroll=on_scroll
) as listener:
    listener.join()

