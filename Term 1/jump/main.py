import pygame as pg
from settings import *
from game_Class import *

def main():

    pg.init()
    game = Game()
    game.start_game_loop()
    pg.quit()
    quit

main()