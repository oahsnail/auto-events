from pynput import mouse, keyboard
from pynput.mouse import Controller as MouseController, Button as MouseButton
from pynput.keyboard import Controller as KeyController, Key, Listener, KeyCode
from tkinter import *
import time
import threading


mouse = MouseController()
keyboard = KeyController()
keyCode = KeyCode()


def pressLeftClick():
    mouse.press(MouseButton.left)


def releaseLeftClick():
    mouse.release(MouseButton.left)


def end():
    keyboard.press(Key.end)


def onPress(key):
    print(str(key) + " pressed")
    if(key == Key.end):
        releaseLeftClick()
        return False
    if(key == Key.up):
        pressLeftClick()
    if(key == Key.down):
        releaseLeftClick()


def onRelease(key):
    if(key == Key.end):
        return False
    if(key == keyCode.from_char("k")):
        print("ooga booga")


def startListen():
    print("started")
    with Listener(on_press=onPress, on_release=onRelease) as listener:
        listener.join()


def startThread():
    threading.Thread(target=startListen).start()


def onClosing():
    end()
    root.destroy()


# gui stuff
root = Tk()
root.title("Auto-Events")
frame = Frame(root)
frame.pack()
startButton = Button(frame, text="Start Listening",
                     command=startThread)
stopButton = Button(frame, text="Stop Listening", command=end)

startButton.pack()
stopButton.pack()

root.protocol("WM_DELETE_WINDOW", onClosing)
root.mainloop()
