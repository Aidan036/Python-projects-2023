def write_Question(list, open_file):
   for i in list:
      open_file.write(i+"\n")

   open_file = open("exams/ExampleTest.txt", "w")
   open_file.write("Aidan Pearce pyton term 2 final exam\n")

question1 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question2 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question3 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question4 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question5 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question6 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question7 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question8 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question9 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question10 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question12 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question13 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question14 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question15 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question16 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question17 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question18 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question19 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question20 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question21 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question22 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question23 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question24 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]
question25 = ["category","Question","option 1","option 1","option 1","option 1","answer","exp"]

questions = [question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,question12,question13,question14,question15,question16,question17,question18,question19,question20,question21,question22,question23,question24,question25]



open_file = open("exams/ExampleTest.txt", "r")
list = open_file.readlines()
print(list)

for i in range(len(list)):
   list[i] = list[i].strip("\n")

print(list)
open_file.close()

open_file = open("exams/ExampleTest.txt", "w")
open_file.write("Aidan Pearce pyton term 2 final exam\n")
open_file.write("Question Category\n")
open_file.write("What is the Question to ask?\n")
open_file.write("Option 1\n")
open_file.write("Option 2\n")
open_file.write("Option 3\n")
open_file.write("Option 4\n")
open_file.write("answer\n")
open_file.write("explanation\n")
for i in range(24):
   open_file.write("""category
   question
   option 1
   option 2
   option 3
   option 4
   answer
   explanation
   """)



open_file.close()