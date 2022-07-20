from time import sleep
from PIL import ImageGrab
import pyautogui

def checkforload():
    screen = ImageGrab.grab(bbox=bbox)
    loading = False
    for x in range(screen.width):
        for y in range(screen.height):
            if screen.getpixel((x, y)) == color:
                loading = True
                break
    return(loading)

def pause():
    pyautogui.press("p") #Insert your pause button here
    sleep(4)

color = (255, 255, 255)
width, height= pyautogui.size()
bbox = (width-70, height-70, width-50, height-50)
going = True
timing = False
pause()
while True:
    timing = checkforload()
    if timing == going:
        pause()
        if going:
            going = False
        else:
            going = True
