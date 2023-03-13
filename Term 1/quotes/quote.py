# Aidan Pearce
# 9/8/2022
# Inspirational quote generator

# imports
import random

# global Variables
Welcomes = ["top of the morning to you","Good Morning","Have A Splendid Morning",

quotes = ["top of the morning to you","Good Morning","Have A Splendid Morning",]

names =[]            
            
quote_1 = "\"Success is not final, failure is not fatal: it is the courage to continue that counts.\" "
quote_1_name = "Winston Churchill"
quote_2 = "You don't always need a plan. Sometimes you just need to breathe, trust, let go and see what happens."
quote_2_name = "Mandy Hale"
quote_3 = "I'm not going to continue knocking that old door that doesn't open for me. I'm going to create my own door and walk through that."
quote_3_name = "Ava DuVernay"
quote_4 = "Just don't give up trying to do what you really want to do. Where there is love and inspiration, I don't think you can go wrong."
quote_4_name = "Ella Fitzgerald"

# functions
def quote_card(quote,name):
    size =  len(quote)+5 # get the size of the quote and add 5 to it
    welcome  =  random.choice(welcomes)
    print()
    print()
    print()
    print()
    print()
    print()
    print("\t\t\t\t"+"="*(size)+" ")
    print("\t\t\t\t|"+" "*(size - 2)+"|")
    print("\t\t\t\t|"+welcome+" "*(size-len(welcome)-2)+"|")
    print("\t\t\t\t|"+quote+" "*(size-len(quote)-2)+"|")
    print("\t\t\t\t| \t---"+name+" "*(size-len(name)-12)+"|")
    print("\t\t\t\t|"+" "*(size - 2)+"|") 
    print("\t\t\t\t|"+" "*(size - 2)+"|")
    print("\t\t\t\t|"+" "*(size - 2)+"|")
    print("\t\t\t\t"+"="*(size)+" ")
    

# main
def main():
    # build program
    number = random.randint(0,len(quotes)-1)
    quote_card(Quotes[number],names[number])
   
    #print(len(quote_3))
    
main()

#hold program open until user hits enter
input()
