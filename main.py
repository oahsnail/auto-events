import threading
import time
import tkinter as tk

from pynput import keyboard, mouse
from pynput.keyboard import Controller as KeyController
from pynput.keyboard import Key, KeyCode, Listener
from pynput.mouse import Button as MouseButton
from pynput.mouse import Controller as MouseController

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
root = tk.Tk()
root.title("Auto-Events")
frame = tk.Frame(root)
frame.pack()
instructions = tk.Label(
    root, text="""Press \"start listening\" button to start the program.
                  Press up-arrow to hold click, and down-arrow to release click. 
                  Press \"stop-listening\" or the \"end\" key to pause the program""")

startButton = tk.Button(frame, text="Start Listening",
                        command=startThread)
stopButton = tk.Button(frame, text="Stop Listening", command=end)

instructions.pack()
startButton.pack()
stopButton.pack()

root.protocol("WM_DELETE_WINDOW", onClosing)
root.mainloop()
