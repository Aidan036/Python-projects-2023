from game import *

def main():
    while True:
        game()
        if guesses < len(HangMan):
            print("you win")
        else:
            print("you lose")

        answer = input("do you want to play again Y/N")
        if answer.upper()

main()