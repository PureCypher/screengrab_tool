"""
Auto ScreenGrabber for Windows PC
        PureCypher
"""
import pyautogui
import time

screenpath = 0

while True:
    screenpath += 1
    myScreenShot = pyautogui.screenshot()
    myScreenShot.save(r"C:\\Users\\User\\Desktop\\LOLz\\" + str(screenpath) + ".png")
    time.sleep(30)
