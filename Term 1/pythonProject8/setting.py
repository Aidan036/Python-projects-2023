from tkinter import *
import random
import datetime
from tkinter import ttk
from os import path


HEIGHT = 1080
WIDTH = 1920
SCREEN_SIZE = str(WIDTH)+"x"+str(HEIGHT)\

title = "Christmas CountDown"

LOCATION = path.dirname(__file__)
img_folder = path.join(LOCATION,"imgs")
b_day_folder = path.join(img_folder,"b_day_imgs")
pic_folder = path.join(img_folder,"pic_imgs")
july_4_folder = path.join(img_folder,"independance_day_imgs")
newyears_folder = path.join(img_folder,"newyears_imgs")

pic_img_list = []
for i in range(1):
    pic_img_list.append(str.format("pic{}.png",i+1))

b_day_img_list = []
for i in range(5):
    b_day_img_list.append(str.format("b_day{}.png",i+1))

july_4_img_list = []
for i in range(5):
    july_4_img_list.append(str.format("4_july{}.png",i+1))

newyears_img_list = []
for i in range(5):
    newyears_img_list.append(str.format("ny{}.png",i+1))