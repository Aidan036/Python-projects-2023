import BlackJack_Classes
from cards_file import *
from player_file import *
import random





def main():
    game = BlackJack_Classes.BlackJack_Game(["Tim","Bob","Joe"])
    game.play()

main()