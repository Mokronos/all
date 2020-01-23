import numpy as np
import cv2
from PIL import ImageGrab
import win32api, win32con, win32gui
import time
print(win32gui.GetCursorPos())

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def find(img):
    for i in range(30):
        for j in range(90):
            if img.getpixel((i,j))!=(48, 52, 67):
                print("pod")
                return True
    return False
while(True):
    click(1192,646)
    time.sleep(0.05)
    img = ImageGrab.grab(bbox=(1070,660,1100,750))
    print(img.getpixel((5,5)))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
#    cv2.imshow("test", img_np)
    if find(img)==True:
        click(-200,200)
        input("Pod found ... Press key to continue searching")

#    cv2.waitKey(0)

cv2.destroyAllWindows()

