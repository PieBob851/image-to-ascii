import sys

f = open("out.txt", "wt", encoding="utf-8")
sys.stdout = f

resize_factor = 20 #the factor with which to scale the width and height of the image
image_name = "image.png" #the name of the image file to convert

from PIL import Image, ImageFilter
import numpy as np

image = Image.open(image_name).convert('L')
nHeight, nWidth = int(image.height/resize_factor), int(image.width/resize_factor)
imgarr = np.asarray(image.resize((nWidth,nHeight)))

maximum = 0
minimum = 256

for y in range(nHeight):
    for x in range(nWidth):
        maximum = max(maximum, imgarr[y][x])
        minimum = min(minimum, imgarr[y][x])

thresholds = [maximum - (maximum - minimum)/11*(i+1) for i in range(10)]

for y in range(nHeight):
    for x in range(nWidth):
        if imgarr[y][x] > thresholds[0]:
            print("  ", end="")
        elif imgarr[y][x] > thresholds[1]:
            print(". ", end="") 
        elif imgarr[y][x] > thresholds[2]:
            print("- ", end="") 
        elif imgarr[y][x] > thresholds[3]:
            print("* ", end="") 
        elif imgarr[y][x] > thresholds[4]:
            print("= ", end="") 
        elif imgarr[y][x] > thresholds[5]:
            print("+ ", end="") 
        elif imgarr[y][x] > thresholds[6]:
            print("| ", end="") 
        elif imgarr[y][x] > thresholds[7]:
            print("# ", end="") 
        elif imgarr[y][x] > thresholds[8]:
            print("░ ", end="") 
        elif imgarr[y][x] > thresholds[9]:
            print("▒ ", end="") 
        else:                   
            print("▓ ", end="")
    print()   

f.close()
