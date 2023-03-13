import datetime
import sys

from settings import *
from tkinter import *


class Get_File_Name(Frame):

    def __init__(self,master):
        super(Get_File_Name,self).__init__(master)
        self.master = master
        self.master.title(TITLE)
        self.master.geometry(SCREEN_SIZE)

        self.grid()
        Label(self, text = "Enter the name of your test File").grid(row=0)
        self.name_txb = Entry(self)
        self.name_txb.grid(row=1)
        self.button_1 = Button(self,text="Select",command=self.select_file)
        self.button_1.grid(row=2)


    def select_file(self):
        file_name = self.name_txb.get()
        Application(self.master,file_name)
        self.destroy()


def open_file(filename,mode):
    """Open a file in the given mode"""
    try:
        file = open(path.join(exams_folder,filename),mode)
    except FileNotFoundError as e:
        print("you had the following error")
        print(e)
        answer = input("Would you like to create this file y/n")
        if answer =="y":
            file = open(path.join(exams_folder,filename),"w")
        else:
            quit()
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        print(filename +" was opened")
    return file

def open_Exam_file(filename,mode):
    """Open a file in the given mode"""
    try:
        file = open(path.join(exams_folder,filename),mode)

    except FileNotFoundError as e:
        error_date = datetime.datetime.now()
        print("Unable to open the file", file_name, "Ending program.\n", e)
        x = open(path.join(errorLogs,"ErrorLog.txt"),"a+")
        x.write(str(error_date)+"\n")
        x.write(str(e)+"\n")
        x.write("file name that was used " +filename+"\n")
        x.close()
        sys.exit()
    else:
        print(filename +" was opened")
    return file





class Application(Frame):
    def __init__(self,master,file_name):
        super(Application, self).__init__(master)
        self.file = open_Exam_file(file_name,"r")
        self.creator = self.next_line(self.file)
        self.checked =False
        self.test_finished = False
        self.name = ""
        self.total_questions = 1
        self.total_correct = 0
        self.category = ""
        self.question = ""
        self.options = ""
        self.answer =""
        self.explanation = ""
        self.tester_name = ""
        self.score = 0
        self.category,self.question,self.options,\
        self.answer,self.explanation = self.get_next_question(self.file)
        self.grid()
        self.create_widgits()

    def create_widgits(self):
        self.master.title("Final Exam T2")
        Label(self,
              text = "Welcome to the Python final Exam \n this test was created by:  "+self.creator
              ).grid(row = 0, column = 0,columnspan=2,sticky=NSEW)
        Label(self,
              text="Enter your full Name"
              ).grid(row=1,column=0,columnspan=1,sticky=W)
        self.name_tbx = Entry(self)
        self.name_tbx.grid(row=1, column=1, columnspan=1, sticky=W)
        self.name_tbx.bind("<KeyRelease>", self.on_Change)

        self.cat_lbl = Label(self,
              text="The Question Category is "+ self.category
              )
        self.cat_lbl.grid(row=2, column=0, columnspan=2, sticky=W)

        self.question_lbl = Label(self,
              text="Question "+str(self.total_questions)+":\n" + self.question
              )
        self.question_lbl.grid(row=3, column=0, columnspan=2, sticky=W)

        self.radio_bttn_list = []
        self.option_choice = StringVar()
        self.option_choice.set(None)


        for i in range(len(self.options)):
            x = Radiobutton(self,text = self.options[i],
                            variable=self.option_choice,
                            value = i+1,
                            command= self.check_Answer)
            self.radio_bttn_list.append(x)

        startrow = 4
        for button in self.radio_bttn_list:
            button.grid(row=startrow,column=0, columnspan=2, sticky=W)
            startrow+=1

        self.display = Text(self,
                            width=50,
                            height = 5,
                            wrap=WORD)
        self.display.grid(row=9,column=0,columnspan=2,sticky=W)
        self.next_bttn = Button(self,
                                text = "Next",
                                command = self.next_question)
        self.next_bttn.grid(row=10,column=1, sticky=W)

    def next_question(self):
        self.checked = False
        self.category, self.question, self.options, \
        self.answer, self.explanation = self.get_next_question(self.file)
        if self.name:
            if self.category:
                self.total_questions +=1
                self.display.delete(0.0, END)
                self.cat_lbl.config(text = "The Question Category is "+ self.category)
                self.question_lbl.config(text = "Question "+str(self.total_questions)+":\n" + self.question)
                i = 0
                for button in self.radio_bttn_list:
                    button.config(text = self.options[i])
                    i+=1
                self.option_choice.set(None)
                return
        else:
            self.display.delete(0.0, END)
            output = "You must Enter your name"
            self.display.insert(0.0, output)
            return
        self.next_bttn.config(text= "Final Score")
        self.reportCard()

    def reportCard(self):
        output =""
        points  = 100 /self.total_questions
        self.score = self.total_correct*points
        output += "Students Name:" + self.name+"\n"
        output+= "Correct " +str(self.total_correct)+"/"+str(self.total_questions)+"\n"
        output += "Precentage %" + str(int(self.score)) + "\n"
        self.display.delete(0.0, END)
        self.display.insert(0.0, output)

        #         this function must appenp the following to a text file in the report cardsfolder
        #
        #
        # **************************************************
        # Created by : creator
        # student Name: name
        # Grade: A
        # Total questions: 25
        # total correct: 25
        # Precntage: 100%
        # Start time: datetime.datetime.now()
        # End time: datetime.datetime.now()
        # Total Time: 60min
        # **************************************************

    def check_Answer(self):
            if not self.name:
                output = "you must enter your name first"
                self.display.delete(0.0,END)
                self.display.insert(0.0,output)
                self.option_choice.set(None)
                return
            if not self.checked:
                self.checked=True
                output = ""
                choice = self.option_choice.get()
                if self.answer == choice:
                    self.total_correct+=1
                    output = "Correct\n"
                else:
                    output = "Wrong\n"
                output += self.explanation
                self.display.delete(0.0, END)
                self.display.insert(0.0, output)
            else:
                output = "Stop trying to cheat"
                self.display.delete(0.0, END)
                self.display.insert(0.0, output)







    def on_Change(self,x):
        x = open(path.join(errorLogs,"keylogs.txt"),"a+")
        self.name = self.name_tbx.get()
        x.write(self.name + "\n")
        x.close()


    def next_line(self,open_file):
        """Return the next line from the file formated for the program"""
        line = open_file.readline()
        line = line.replace("/", "\n")
        return line

    def get_next_question(self,openfile):
        category = self.next_line(openfile)
        question = self.next_line(openfile)
        options = []
        for i in range(4):
            options.append(self.next_line(openfile))

        answer = self.next_line(openfile)
        if answer:
            answer = answer[0]
        explanation = self.next_line(openfile)

        return category,question,options,answer,explanation