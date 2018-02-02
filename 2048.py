from pygame.locals import *
from random import randint

import pygame
import time

# Board Class
# this will hold all the board and movement performed on
# on the board
class Board:
    # create a list of element
    boards = []
    x = 0
    y = 0

    # x, and y will determine the length of the board
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # create the 2d list of the boards based on the x and y
        # value passed to the initialization
        for i in range(0, x):
            # apend a list to the boards
            self.boards.append([]);

        for i in range(0, x):
            for j in range(0, y):
                self.boards[i].append(0);

    def printBoard(self):
        print(self.boards)

    def moveLeft(self):
        print("Move Left")

    def moveRight(self):
        print("Move Right")

    def moveUp(self):
        print("Move Up")

    def moveDown(self):
        print("Move Down")

class App:
    windowWidth = 800
    windowHeight = 600

    def __init__(self):
        # set that running indicator into true
        self._running = True

        # create the display surface.
        # we will fill this display with the display from the pygame during oninit
        self._display_surf = None

        # create the variable for boards
        self.board = Board(4,4)

    def on_init(self):
        # init pygame
        pygame.init();

        # set the display surface for the program
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        # set the title of the program
        pygame.display.set_caption('2048 Game on Python')

        # set the running indicator into true
        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        # for test purpose only
        # self.board.printBoard()
        pass

    def on_render(self):
        # fill the window screen with black
        self._display_surf.fill((0,0,0))
        pygame.display.flip()
        print("Rendering game...")

    def on_cleanup(self):
        # quit the program
        pygame.quit()

    def on_execute(self):
        # check whether we can perform initialization on the pygame or not?
        if self.on_init() == False:
            self._running = False

        # check for keyboard input if the game is still running
        while(self._running):
            pygame.event.pump()

            events = pygame.event.get()
            for event in events:
                if (event.type == pygame.KEYDOWN):
                    keys = event.key
                
                    if (keys == pygame.K_RIGHT):
                        self.board.moveRight()
                        
                    if (keys == pygame.K_LEFT):
                        self.board.moveLeft()

                    if (keys == pygame.K_UP):
                        self.board.moveUp()

                    if (keys == pygame.K_DOWN):
                        self.board.moveDown()

                    if (keys == pygame.K_ESCAPE):
                        self._running = False

                    #self.on_loop()
                    self.on_render();

            time.sleep (100.0 / 1000.0);

        self.on_cleanup()

# main procedure
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
            
