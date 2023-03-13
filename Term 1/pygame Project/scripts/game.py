from scripts.settings import *
from scripts.player import *
from scripts.enemy import *


class Game(object):

    def __init__(self):
        self.playing = True
        pg.init()
        pg.mixer.init() # if using replit comment this out and anything else that uses sound at all
        # set up game screen
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        #pg.display.set_icon()
        self.clock = pg.time.Clock()

        # create sprite groups
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.player_group = pg.sprite.Group()



        # create player as a player object
        self.player = Player(self)

        # create enemies

    def gameLoop(self):
        while self.playing:
            # tick clock
            self.clock.tick(fps)
            # check events
            self.checkEvents()
            # update all
            self.update()
            # draw
            self.draw()

    def checkEvents(self):
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.playing = False

    def update(self):
        self.all_sprites.update()
    def draw(self):
        self.screen.fill(DEFAULT_COLOR)
        self.all_sprites.draw(self.screen)

        # must be the last line in draw section
        pg.display.flip()

    def startScreen(self):
        pass
    def endScreen(self):
        pass
