from scripts.settings import *


class Player(pg.sprite.Sprite):

    def __init__(self,game):
        super(Player, self).__init__()
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)

        game.all_sprites.add(self)
        game.player_group.add(self)


    def update(self):
        self.rect.x += 1