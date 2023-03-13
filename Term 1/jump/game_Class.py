import pygame
import random
from settings import *
from game_Objects import *


class Controller():
    def __init__(self,cont_number=0):
        try:
            self.controller = pg.joystick.Joystick(cont_number)
            self.controller.init()
            try:
                cont_id = self.controller.get_id()
            except AttributeError:
                cont_id = self.controller.get_id()
        except IOError:
            print("no controller connected")
    def get_hat(self):
        hat = self.controller.get_hat(0)
        x = hat[0]
        y = hat[1]*-1
        # dictionary (stores key value pairs)
        hat_dict = {"H_X":x,"H_Y":y}
        return hat_dict

    def get_buttons(self):    
        a_button = self.controller.get_button(0)

        buttons_dict = {"CONT_A":a_button,}
        return buttons_dict

class Game():

    def __init__(self):
        self.playing = True
        self.game_window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        joystick_count = pg.joystick.get_count()

        # set up controller if one is connected
        if joystick_count > 0:
            self.xbox_controller = Controller()
        else:
            self.xbox_controller = None

        self.background_img = GameObject(0,0,WIDTH,HEIGHT,bgimg_location)
        self.treasure_img = GameObject(WIDTH/2-tile_size/2,tile_size/3,tile_size,tile_size,trimg_location)
        self.player = Player(player_start_pos_x,player_start_pos_y,tile_size,tile_size,player_img,player_speed)
        self.enemies_list = []
        self.spawn_enemies(4)
        self.spawn_enemies2(4)


    def spawn_enemies(self,num):
        start = 0
        for i in range(num):
            enemy_x = random.randint(0,WIDTH-tile_size)
            start += 200
            enemy_y = start
            flip = random.choice(("h","t"))
            speed = random.randint(8,15)
            if flip == "t":
                speed *= -1
            enemy = Enemy(enemy_x,enemy_y,tile_size,tile_size,enemy_img,speed)
            self.enemies_list.append(enemy)
    def spawn_enemies2(self,num):
        start = 0
        for i in range(num):
            enemy2_x = random.randint(0,HEIGHT-tile_size)
            start += 190
            enemy2_y = start
            flip = random.choice(("h","t"))
            speed = random.randint(8,15)
            if flip == "t":
                speed *= -1
            enemy2 = Enemy(enemy2_x,enemy2_y,tile_size,tile_size,enemy2_img,speed)
            self.enemies_list.append(enemy2)

    def start_game_loop(self):
        while self.playing:
            # tick Clock
            self.clock.tick(fps)
            # get inputs
            self.get_inputs()
            # update
            self.update()
            # draw
            self.draw()





    def get_inputs(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.playing = False
        self.get_player_inputs(events)

    def update(self):
        self.player.move()

        for enemy in self.enemies_list:
            enemy.move(WIDTH)

        if self.detect_Collision(self.player,self.goal):
            print("player has won")

        for enemy in self.enemies_list:
            if self.detect_Collision(self.player,enemy):
                self.playing = False
                print("player has lost")

    def draw(self):
        self.game_window.fill(purple)
        self.game_window.blit(self.background_img.image, (self.background_img.x, self.background_img.y))
        self.game_window.blit(self.treasure_img.image, (self.treasure_img.x, self.treasure_img.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        for enemy in self.enemies_list:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
            #self.game_window.blit(enemy2_img.image, (enemy2_img.x, enemy2_img.y))

        pg.display.update()

    def get_player_inputs(self,events):
        if self.xbox_controller :
            hat = self.xbox_controller.get_hat()
            self.player.set_move_dir(hat.get("H_X"),hat.get("H_Y"))


        for event in events:

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w or event.key == pg.K_UP:
                    self.player.set_move_dir(0, -1)
                if event.key == pg.K_s or event.key == pg.K_DOWN:
                    self.player.set_move_dir(0, 1)
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    self.player.set_move_dir(-1, 0)

                if event.key == pg.K_d or event.key == pg.K_RIGHT:
                    self.player.set_move_dir(1, 0)
                if event.key == pg.K_RSHIFT or event.key == pg.K_LSHIFT:
                    self.player.speed *= sprint_mod

            if event.type == pg.KEYUP:
                if event.key == pg.K_w or event.key == pg.K_UP or event.key == pg.K_s or event.key == pg.K_DOWN or event.key == pygame.K_a or event.key == pg.K_LEFT or event.key == pg.K_d:
                    self.player.set_move_dir(0,0)
                if event.key == pg.K_RSHIFT or event.key == pg.K_LSHIFT:
                    self.player.speed /= sprint_mod

    def detect_Collision(self,obj1,obj2):
#           check if colliding in the x dir
        if obj1.x > (obj2.x + obj2.width):
            return False
        elif (obj1.x + obj1.width) < obj2.x:
            return False

        if obj1.y > (obj2.y + obj2.height):
            return False
        elif (obj1.y + obj1.height) < obj2.y:
            return False

        return True