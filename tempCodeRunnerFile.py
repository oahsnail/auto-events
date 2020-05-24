from pynput import mouse, keyboard
from pynput.mouse import Controller as MouseController, Button as MouseButton
from pynput.keyboard import Controller as KeyController


mouse = MouseController()


def leftClick():
    mouse.click(MouseButton.left, 1)


def stopper():
    testTimer = 0
    while(testTimer < 1000):
        leftClick()
        testTimer += 1


stopper()
