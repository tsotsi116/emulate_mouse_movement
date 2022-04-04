from random import randint
from pyautogui import moveTo, size
from time import sleep

screenWidth, screenHeight = size()

while True:
    wPosition = randint(0, screenWidth)
    hPosition = randint(0, screenHeight)
    print(wPosition, hPosition)
    moveTo(wPosition, hPosition, 5)
    sleep(60)
