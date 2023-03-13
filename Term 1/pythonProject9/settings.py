from tkinter import *
from os import path

HEIGHT = 420
WIDTH = 640

TITLE = "Term 2 Final Exam"

SCREEN_SIZE = str(HEIGHT)+"x"+str(WIDTH)

file_name = "test.txt"

location = path.dirname(__file__)
exams_folder = path.join(location,"exams")
reports_folder = path.join(location,"reports")
errorLogs = path.join(reports_folder,"errorLogs")
report_Cards = path.join(reports_folder,"reportCards")

test = path.join(exams_folder,file_name)

