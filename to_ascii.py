#!/bin/python3

from PIL import Image
from tkinter import filedialog as fd

ascii_char = " @B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`\'.               "

def get_char(r, b, g, alpha=256):
    length = len(ascii_char)
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)
    unit = (256.0+1)/length
    return ascii_char[-1* int(gray/unit)]


filename = fd.askopenfilename(title='Pick file to convert', initialdir='.', filetypes=(('Images','*.png *.jpg'),('All files','*.*')))
if filename == '': exit()

image = Image.open(filename)

ratio = 30
width, height = image.size
nHeight = int(height * (ratio/100) / 1.65)
nWidth = int(width * (ratio/100) )
print(nWidth, nHeight)

image = image.resize((nWidth, nHeight), Image.NEAREST)

ascii_image = ""
for i in range(nHeight):
    for j in range(nWidth):
        ascii_image += get_char(*image.getpixel((j,i)))
    ascii_image += '\n'


print(ascii_image)

with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)


