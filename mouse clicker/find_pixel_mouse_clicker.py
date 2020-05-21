#import numpy
from PIL import ImageGrab, ImageOps
import pyautogui



screen_coords = [80, 330, 300, 470]
pixel_coords = (0,0)

        

#print(pyautogui.displayMousePosition())
image = ImageGrab.grab(bbox=screen_coords)
grayImage = ImageOps.grayscale(image)
for x in range(220):
    for y in range(140):
        cur_pos = (x,y)
        pixel = grayImage.getpixel(cur_pos)
        #print(pixel)
        if(pixel > 10):
            print("znaleziono")

def main():


if __name__ = "__main__":
    main()
