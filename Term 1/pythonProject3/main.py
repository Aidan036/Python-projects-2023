# Aidan Pearce
# 10/6/22
# Choice Board Game

import requests

# functions
print("Hello, welcome to Dentair")
print("you are currently laying down in the middle of a field there is a sword next to you")
print("will you get up or fall back asleep?")

# global variables


# main
import random

def gameLoop(story,question,options1,options2,insults):
    while True:
        print(story)
        while True:
            choice = input(question)
            if(choice in options1):
                story = "option 1"
                break
            elif choice == "fall back asleep": vy
                story = "option 2"
                break
            else:
                print(random.choice(insults))




gameLoop("starting","give me an input",[1,"one","yes"],[2,"two","no"],["you suck try again","it really isnt that hard to figure out","how did you even manage to do that?"])

