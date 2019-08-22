from pygame.locals import *
from random import randint
import pygame
from pygamePlayer import Player
from machine import Machine
import time

class Apple:
    x = 0
    y = 0
    step = 67

    def __init__(self, x, y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))

class Game:
    def isCollision(self, x1, y1, x2, y2, bsize):
        if x2 <= x1 <= x2 + bsize:
            if y2 <= y1 <= y2 + bsize:
                return True
        return False

class App:
    windowWidth = 1500
    windowHeight = 600
    player = 0
    apple = 0

    def __init__(self):
        self._running = True
        self._display_surf = None   # create the display window and display variables for the objects being displayed
        self._player_surf = None
        self._apple_surf = None
        self._machine_surf = None
        self.game = Game()          # game object for collisions
        self.player = Player(4)     # initialize snake with length 5
        self.apple = Apple(3, 0)    # initialize apple directly in front of the snake
        # self.machine = Machine('easy')    # initialize the machine and its difficulty

    def on_init(self):
        pygame.init()   # initialize the window
        self._display_surf = pygame.display.set_mode([self.windowWidth, self.windowHeight])     # set bounds of the window
        self._running = True
        self._player_surf = pygame.image.load("snakePiece.jpg").convert_alpha()     # store the snake image as a variable
        self._apple_surf = pygame.image.load('apple.png').convert_alpha()          # store the apple image as a variable
        # self._machine_surf = pygame.image.load("machinePiece.jpg").convert_alpha()     # store the machine image as a variable

    def on_event(self, event):      # not sure what this does, possibly if you press the red X on the window?
        if event.type == QUIT:
            self._running = False

    def on_loop(self):      # checks to see if snake has collided with anything, displays positions if collision occurs
        self.player.update()    # updates the position of the player
        # self.machine.update() # updates the position of the machine

        # does snake eat apple? note, if apple spawns in a x,y position that some part of the snake is currently at
        #                       the snake should eat it anyways
        self._is_collision_apple()

        # does snake collide with itself?
        self.is_collision_self()

        # does snake collide with walls?
        self.is_collision_wall()

        # does the player collide with the machine?
        # self.is_collision_machine()

        # does the machine collide with the player?
        # self.is_collision_player()

        pass

    def is_collision_self(self):
        for i in range(2, self.player.length): # doesn't start at 0 because snake head cant collide with itself
            if self.game.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 40):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                print("Apple Position: " + str(self.apple.x) + ", " + str(self.apple.y))
                exit(0)

    def is_collision_wall(self):
        if self.player.x[0] < 0 or 0 > self.player.y[0] or self.player.x[0] > self.windowWidth or \
                self.player.y[0] > self.windowHeight:
            print("You lose! Collision with the Wall: ")
            print("Position: (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
            print("Apple Position: " + str(self.apple.x) + ", " + str(self.apple.y))
            exit(0)

    def _is_collision_apple(self):
        for i in range(0, self.player.length):
            if self.game.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], 44):
                self.apple.x = randint(2, 8) * 67
                self.apple.y = randint(2, 8) * 67
                self.player.length = self.player.length + 1

    def on_render(self):       # draws the snake and apple images on the window
        self._display_surf.fill((0, 0, 0))
        self.player.draw(self._display_surf, self._player_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        # self.machine.draw(self._display_surf, self._machine_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):  # game loop
            pygame.event.pump()
            keys = pygame.key.get_pressed()     # determines if a key has been pressed

            # updates the snake position based on the key pressed
            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            # if esc pressed, end the game
            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()

            time.sleep(50.0 / 1000.0)      # game time delay (50 millisecond delay)
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()          # initialize the game
    theApp.on_execute()     # start the game
