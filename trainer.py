import tkinter as tk
import os
from PIL import Image, ImageTk
import numpy as np
import random

SIZEX = 320
SIZEYNOL = 294
SIZEYL = 400
ROWS=5
COLS = 11
badcords = [(1,0),(2,0),(3,0),(4,0),(2,1),(1,3),(3,3)]
sprite_array = np.zeros((ROWS,COLS),dtype=(float,4))
sprite_array_name = np.zeros((ROWS,COLS),dtype=(float,4))
root_dir = os.path.dirname(os.path.realpath(__file__))
image_dir = os.path.join(root_dir,"Resources")
hiragana_image = Image.open(os.path.join(os.path.abspath(image_dir),"Table_hiragana.png"))
katakana_image = Image.open(os.path.join(os.path.abspath(image_dir),"Table_katakana.png"))
dim = hiragana_image.size
for y in range(ROWS):
    #print("y:",y * (dim[1]/ROWS),(y+1) * dim[1]/ROWS)
    for x in range(COLS):
        sprite_array[y][x] = (x * (dim[0]/COLS),y * (dim[1]/ROWS),(x+1) * dim[0]/COLS,(y+1) * dim[1]/ROWS - 106)
        sprite_array_name[y][x] = (x * (dim[0]/COLS),y * (dim[1]/ROWS),(x+1) * dim[0]/COLS,(y+1) * dim[1]/ROWS)
        #print("x:",x * (dim[0]/COLS),(x+1) * dim[0]/COLS)


window = tk.Tk()
window.geometry("640x400")
letters = False
hiraimage = hiragana_image.crop(sprite_array[0][0]),(0,0,SIZEX,SIZEYNOL)
kataimage = katakana_image.crop(sprite_array[0][0]),(SIZEX,0,SIZEX*2,SIZEYNOL)
hirapluskata = Image.new("RGB",(SIZEX*2,SIZEYL),"white")
hirapluskata.paste(hiraimage[0],(0,0,SIZEX,SIZEYNOL))
hirapluskata.paste(kataimage[0],(SIZEX,0,SIZEX*2,SIZEYNOL))
     
bild = ImageTk.PhotoImage(hirapluskata)
test = tk.Label(image=bild)     
test.pack()
row = 0
col = 0
def changeimage(e):
    global letters
    global row
    global col
    #print(row,col)
    validcord = False
    if letters == True:
        while not(validcord):
            row = random.randrange(5)
            col = random.randrange(11)
            '''
            if row < 4:
                row += 1
            elif col < 10:
                row = 0
                col += 1
            else: 
                row= 0
                col = 0
            '''
            if (row,col) not in badcords:
                validcord = True
        hiraimage = hiragana_image.crop(sprite_array[row][col]),(0,0,SIZEX,SIZEYNOL)
        kataimage = katakana_image.crop(sprite_array[row][col]),(SIZEX,0,SIZEX*2,SIZEYNOL)
        hirapluskata = Image.new("RGB",(SIZEX*2,SIZEYL),"white")
        hirapluskata.paste(hiraimage[0],(0,0,SIZEX,SIZEYNOL))
        hirapluskata.paste(kataimage[0],(SIZEX,0,SIZEX*2,SIZEYNOL))
        bild = ImageTk.PhotoImage(hirapluskata)
        test.configure(image=bild)
        test.image = bild
        letters = False
    else:
        hiraimage = hiragana_image.crop(sprite_array_name[row][col]),(0,0,SIZEX,SIZEYL)
        kataimage = katakana_image.crop(sprite_array_name[row][col]),(SIZEX,0,SIZEX*2,SIZEYL)
        hirapluskata = Image.new("RGB",(SIZEX*2,SIZEYL),"white")
        hirapluskata.paste(hiraimage[0],(0,0,SIZEX,SIZEYL))
        hirapluskata.paste(kataimage[0],(SIZEX,0,SIZEX*2,SIZEYL))
        bild = ImageTk.PhotoImage(hirapluskata)
        test.configure(image=bild)
        test.image = bild
        
        letters = True
     

window.bind("<space>",changeimage)
window.mainloop()