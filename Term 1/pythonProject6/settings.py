
from game import *
import settings as settings


def main():
    while True:
        choice  = settings.display_menu(["Play Tic Tac Toe","Play Hang Man","Rock paper Scsissors","Quit"],"what would you like to do?")

        if choice == 1:
            game_TicTacToe()
        elif choice == 2:
            game_hangman()
            if settings.guesses < len(settings.HANGMAN):
                print("you win good job")
            else:
                print("you lose")
        elif choice == 3:
            rock_paper_scissors()
        else:
            settings.game_quit()






guesses = 0
HANGMAN = ("""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
"""
)
max_guess = len(HANGMAN)-1
WORDS = ("if","else","loop","tuple","list","function","method","class","attribute","python","guido van rossum","zen","boolean","recursive","syntax","runtime","logic","int","float","string")


# tic tac toe settings
MAX_SPOTS = 9
X = "X"
O = "O"
E = " "

def display_menu(options,question):
    for i in range(len(options)):
        print(str.format("\t({0}.) ------------- {1:<30}",i+1,options[i]))
    while True:
        choice = getNumberInRange(question,1,len(options))

        return choice


def getNumberInRange(question,min,max):
    while True:
        x = input(question)
        try:
            x = int(x)
        except:
            print("not a number")
            continue
        if x >= min and x <= max:
            return x
        else:
            print("not in Range")

def game_quit():
    choice = display_menu(["Yes","No"],"Are you sure you want to quit?")
    if choice == 1:
        print("Good by")
        input("Press Enter to Continue")
        quit()
    else:
        return

