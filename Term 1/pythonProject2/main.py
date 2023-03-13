# Aidan Pearce
# 9/28/22
# Alarm Clock

from tkinter import *
from tkinter import ttk
from tkinter import font

import time
import calendar
import datetime
import winsound

alh = ""
alm = ""
als = ""
t = ""
fullscreen = True

def gettimeString(alh,alm,als,t):
    timeZone = 10
    cdt = 5
    mdt = 6
    mst = 7
    pdt = 7
    adt = 8
    hast = 10

    total_seconds = calendar.timegm(time.gmtime())
    cur_sec = total_seconds%60
    total_mins = total_seconds//60
    cur_min = total_mins%60
    total_hour = total_mins//60
    cur_hour =total_hour%24

    cur_hour -= mdt
    am_pm_tag = ""
    if cur_hour >= 12:
        cur_hour = cur_hour-12
        am_pm_tag = "PM"

        if cur_hour == 0:
            cur_hour = cur_hour + 12
    else:
        am_pm_tag = "AM"
        if cur_hour == 0:
            cur_hour = cur_hour + 12
    xmin=str(cur_min)
    xsec=str(cur_sec)
    if cur_min < 10:
        xmin = "0"+str(cur_min)
    if cur_sec < 10:
        xsec = "0"+str(cur_sec)

    alarm = str.format("{:2}:{}.{} {} ",alh,alm,als,t)

    timeString = str.format("{:2}:{}.{} {} ",cur_hour,xmin,xsec,am_pm_tag)

    if timeString == alarm:
        alarm_snd()

    return timeString

def alarm_snd():
    for i in range(1):
        winsound.Beep(880, 700),
        winsound.Beep(587, 1000),
        winsound.Beep(698, 500),
        winsound.Beep(880, 500),
        winsound.Beep(587, 1000),
        winsound.Beep(698, 500),
        winsound.Beep(880, 250),
        winsound.Beep(1046, 250),
        winsound.Beep(988, 500),
        winsound.Beep(784, 500),
        winsound.Beep(699, 230),
        winsound.Beep(784, 250),
        winsound.Beep(880, 500),
        winsound.Beep(587, 500),
        winsound.Beep(523, 250),
        winsound.Beep(659, 250),
        winsound.Beep(587, 750)

def show_time():
    global alh
    global alm
    global als
    global t
    time = gettimeString(alh,alm,als,t)
    textvar.set(time)
    root.after(1000,show_time)
def setScreen(x):
        global fullscreen
        fullscreen = not fullscreen
        root.attributes("-fullscreen",fullscreen)

def setAlarm(x):
    global alh
    global alm
    global als
    global t
    alh = input("what hour")
    alm = input("what min")
    als = input("what sec")
    t = input("AM or PM").upper()


root = Tk() # create the tkinter object to work with
root.geometry("450x100")# set size of the window
root.attributes("-fullscreen",fullscreen)# change the full screen setting
root.configure(background='Black') #setting background color
root.bind("x",quit)
root.bind("f",setScreen)
root.bind("a",setAlarm)
root.title("Alarm Clock")
textvar = StringVar()
root.after(1,show_time)
fnt = font.Font(family = "Helvetica",size=60,weight="bold")

lbl = ttk.Label(root,textvariable=textvar,font=fnt,foreground="Teal",background="Black")

lbl.place(relx=0.5, rely=0.5, anchor= CENTER)

root.mainloop()