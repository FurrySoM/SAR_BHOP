from pynput import keyboard
from pynput import mouse
import time
import threading
import pyautogui
import sys
import tkinter
from tkinter import *
import tkinter.messagebox
import inspect
import ctypes

bhopping = False
GJ = False

def _async_raise(tid, exctype):
  """raises the exception, performs cleanup if needed"""
  tid = ctypes.c_long(tid)
  if not inspect.isclass(exctype):
    exctype = type(exctype)
  res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
  if res == 0:
    raise ValueError("invalid thread id")
  elif res != 1:
    # """if it returns a number greater than one, you're in trouble,
    # and you should call it again with exc=NULL to revert the effect"""
    ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
    raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
  _async_raise(thread.ident, SystemExit)

def on_click(x, y, button, pressed):
    global bhopping
    if(button == mouse.Button.right and pressed == True):
        bhopping = True
    elif(button == mouse.Button.right and pressed == False):
        bhopping = False
    elif(button == mouse.Button.middle and pressed == True):
        return False


def bhop():
    global bhopping
    while True:
        if(bhopping == True):
            print("jump")
            pyautogui.press('space')
            time.sleep(0.78)

def on_presskeyboard(key):
    global GJ
    if(key == keyboard.Key.f2):
        GJ = True
    if(key == keyboard.Key.f3):
        GJ = False
        return False

def guaji():
    global GJ
    while True:
        if(GJ == True):
            pyautogui.click(x=1800, y=950)
            time.sleep(0.2)
            pyautogui.keyDown('w')
            time.sleep(0.2)
            pyautogui.keyUp('W')
            pyautogui.keyDown('a')
            time.sleep(0.2)
            pyautogui.keyUp('a')
            pyautogui.keyDown('s')
            time.sleep(0.2)
            pyautogui.keyUp('s')
            pyautogui.keyDown('d')
            time.sleep(0.2)
            pyautogui.keyUp('d')
            time.sleep(0.2)
            pyautogui.click(x=980, y=1030)
            time.sleep(0.2)
            pyautogui.click(x=980, y=950)
            time.sleep(0.2)
            pyautogui.keyDown('w')
            time.sleep(0.2)
            pyautogui.keyUp('W')
            pyautogui.keyDown('a')
            time.sleep(0.2)
            pyautogui.keyUp('a')
            pyautogui.keyDown('s')
            time.sleep(0.2)
            pyautogui.keyUp('s')
            pyautogui.keyDown('d')
            time.sleep(0.2)
            pyautogui.keyUp('d')

def close():
    root.destroy()
    stop_thread(bhopThread)
    exit()

def start_bhop():
    bhopThread = threading.Thread(target = bhop)
    bhopThread.start()
    print("bhopthreadstart")                    
    with mouse.Listener(
            on_click=on_click) as listener:
        tkinter.messagebox.showinfo(title='success',message='press space to bhop')
        listener.join()
    stop_thread(bhopThread)

def start_guaji():
    guajiThread = threading.Thread(target = guaji)
    guajiThread.start()
    with keyboard.Listener(
            on_press=on_presskeyboard) as listener:
        tkinter.messagebox.showinfo(title='success',message='press f2 to guaji')
        listener.join()
    stop_thread(guajiThread)

root = Tk()
root.title('SAR BHOP')
root.geometry('400x200')
btn_start1 = Button(root, text='Bhop', font=("微软雅黑", 12), fg="white", bg="gray", command=start_bhop)
btn_start1.place(relx=0.3, y=15, relwidth=0.4, height=20)
btn_start2 = Button(root, text='挂机', font=("微软雅黑", 12), fg="white", bg="gray", command=start_guaji)
btn_start2.place(relx=0.3, y=45, relwidth=0.4, height=20)
lab0 = Label(root,text='点按钮启动功能',font=("微软雅黑", 12))
lab0.place(relx = 0.1, y= 75, relwidth=0.8, height=20)
lab1 = Label(root,text='按住鼠标右键Bhop',font=("微软雅黑", 12))
lab1.place(relx = 0.1, y= 105, relwidth=0.8, height=20)
lab2 = Label(root,text='按中键关闭Bhop',font=("微软雅黑", 12),fg='black')
lab2.place(relx = 0.1, y= 135, relwidth=0.8, height=20)
lab3 = Label(root,text='点击挂机后F2启动F3关闭功能',font=("微软雅黑", 12))
lab3.place(relx = 0.1, y= 165, relwidth=0.8, height=20)
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
              
              