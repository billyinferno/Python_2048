###########################################################
## 2048 Games in Python                                  ##
## ----------------------------------------------------- ##
## Created by : I Gede Adi Martha Ardiana.               ##
## copyright (c) 2018                                    ##
###########################################################
from pygame.locals import *
from random import randint

import pygame
import time
import math

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
        for i in range(0, y):
            # apend a list to the boards
            self.boards.append([]);

        # clear the board
        self.clearBoard()

        # get 2 random number and put on the board
        self.randomNumber()
        self.randomNumber()

    def clearBoard(self):
        for i in range(0, self.y):
            for j in range(0, self.x):
                self.boards[i].append(0);

    def printBoard(self, surf):
        for y in range(0, self.y):
            for x in range(0, self.x):
                block_image = pygame.image.load("images\\" + str(self.boards[y][x]) + ".png").convert()
                surf.blit(block_image, (10 + (60 * x), 10 + (60 * y)));

    def randomNumber(self):
        # ensure there are blocks that we can filled, before we put randomization
        isZeroTilesAvailable = False
        for y in range(0, self.y):
            for x in range(0, self.x):
                if self.boards[y][x] == 0:
                    isZeroTilesAvailable = True
                    break;

        # check whether we have zero blocks available
        if isZeroTilesAvailable:
            x = randint(0,(self.x-1))
            y = randint(0,(self.y-1))

            while 1:
                if self.boards[y][x] == 0:
                    n = int(math.pow(2,randint(1,3)))
                    self.boards[y][x] = n
                    print("Put " + str(n) +", on block: " + str(x) + "," + str(y) + ".")
                    break
                else:
                    x = randint(0,3)
                    y = randint(0,3);

    def moveLeft(self, surf):
        print("Move Left")

        # set the isMoved as false
        isMoved = False

        # for move left we will shift all x from right most to the nearest
        # boards that empty (value 0)
        for y in range(0,self.y):
            # loop from 1 to 3
            for x1 in range(1,self.x):
                # loop from (x1+1) to 0
                # check if current block on the board is > 0
                if self.boards[y][x1] > 0:
                    # loop from x1-1 to 0
                    currVal = self.boards[y][x1]
                    for x2 in range((x1-1),-1,-1):
                        # check if this is 0 or have equal value with the board
                        if currVal == self.boards[y][x2] and self.boards[y][(x2+1)] == self.boards[y][x2]:
                            # join this two block
                            print("Join Block " + str(x2) + "," + str(y) + " with " + str((x2+1)) + "," + str(y))
                            self.boards[y][x2] = self.boards[y][x2] + currVal
                            self.boards[y][(x2+1)] = 0
                            isMoved = True
                            self.drawBlocks(x2,y,surf)
                            self.drawBlocks((x2+1),y,surf)
                            time.sleep (15.0 / 1000.0)
                            # reset currVal so it will not going to be used to
                            # perform validation for joining the blocks
                            currVal = -1
                        elif self.boards[y][x2] == 0:
                            # move block to left
                            print("Move Block " + str(x2) + "," + str(y) + " to " + str((x2+1)) + "," + str(y))
                            self.boards[y][x2] = currVal
                            self.boards[y][(x2+1)] = 0
                            isMoved = True
                            self.drawBlocks(x2,y,surf)
                            self.drawBlocks((x2+1),y,surf)
                            time.sleep (15.0 / 1000.0)

        return isMoved;

    def moveRight(self, surf):
        print("Move Right")

        # set the isMoved as false
        isMoved = False
        
        # for move right we will shift all x from 0 to x + 1 to the nearest
        # boards that empty (value 0)
        for y in range(0,self.y):
            # loop from 2 to 0
            for x1 in range((self.x-2),-1,-1):
                # check if current block is > 0
                if self.boards[y][x1] > 0:
                    # loop from x1+1 to 3
                    currVal = self.boards[y][x1]
                    for x2 in range(x1+1,self.x):
                        # check if this is 0 or have equal value with the board
                        if currVal == self.boards[y][x2] and self.boards[y][(x2-1)] == self.boards[y][x2]:
                            # join this two block
                            print("Join Block " + str(x2) + "," + str(y) + " with " + str((x2-1)) + "," + str(y))
                            self.boards[y][x2] = self.boards[y][x2] + currVal
                            self.boards[y][(x2-1)] = 0
                            isMoved = True
                            self.drawBlocks(x2,y,surf)
                            self.drawBlocks((x2-1),y,surf)
                            time.sleep (15.0 / 1000.0)
                            # reset currVal so it will not going to be used to
                            # perform validation for joining the blocks
                            currVal = -1
                        elif self.boards[y][x2] == 0:
                            # move block to the right
                            print("Move Block " + str(x2) + "," + str(y) + " to " + str((x2-1)) + "," + str(y))
                            self.boards[y][x2] = currVal
                            self.boards[y][(x2-1)] = 0
                            isMoved = True;
                            self.drawBlocks(x2,y,surf)
                            self.drawBlocks((x2-1),y,surf)
                            time.sleep (15.0 / 1000.0)

        return isMoved;

    def moveUp(self, surf):
        print("Move Up");

        # set the isMoved as false
        isMoved = False

        # for move left we will shift all x from right most to the nearest
        # boards that empty (value 0)
        for x in range(0,self.x):
            # loop from 1 to 3
            for y1 in range(1,self.y):
                # loop from (x1+1) to 0
                # check if current block on the board is > 0
                if self.boards[y1][x] > 0:
                    # loop from y1-1 to 0
                    currVal = self.boards[y1][x]
                    for y2 in range((y1-1),-1,-1):
                        # check if this is 0 or have equal value with the board
                        if currVal == self.boards[y2][x] and self.boards[(y2+1)][x] == self.boards[y2][x]:
                            # join this two block
                            print("Join Block " + str(x) + "," + str(y2) + " with " + str(x) + "," + str(y2 + 1))
                            self.boards[y2][x] = self.boards[y2][x] + currVal
                            self.boards[y2+1][x] = 0
                            isMoved = True
                            self.drawBlocks(x,y2,surf)
                            self.drawBlocks(x,y2+1,surf)
                            time.sleep (15.0 / 1000.0)
                            # reset currVal so it will not going to be used to
                            # perform validation for joining the blocks
                            currVal = -1
                        elif self.boards[y2][x] == 0:
                            # move block to left
                            print("Move Block " + str(x) + "," + str(y2) + " to " + str(x) + "," + str(y2+1))
                            self.boards[y2][x] = currVal
                            self.boards[(y2+1)][x] = 0
                            isMoved = True
                            self.drawBlocks(x,y2,surf)
                            self.drawBlocks(x,(y2+1),surf)
                            time.sleep (15.0 / 1000.0)

        return isMoved;

    def moveDown(self, surf):
        print("Move Down");

        # set the isMoved as false
        isMoved = False
        
        # for move right we will shift all x from 0 to x + 1 to the nearest
        # boards that empty (value 0)
        for x in range(0,self.x):
            # loop from 2 to 0
            for y1 in range((self.y-2),-1,-1):
                # check if current block is > 0
                if self.boards[y1][x] > 0:
                    # loop from y1+1 to 3
                    currVal = self.boards[y1][x]
                    for y2 in range(y1+1,self.y):
                        # check if this is 0 or have equal value with the board
                        if currVal == self.boards[y2][x] and self.boards[(y2-1)][x] == self.boards[y2][x]:
                            # join this two block
                            print("Join Block " + str(x) + "," + str(y2) + " with " + str(x) + "," + str(y2-1))
                            self.boards[y2][x] = self.boards[y2][x] + currVal
                            self.boards[(y2-1)][x] = 0
                            isMoved = True
                            self.drawBlocks(x,y2,surf)
                            self.drawBlocks(x,(y2-1),surf)
                            time.sleep (15.0 / 1000.0)
                            # reset currVal so it will not going to be used to
                            # perform validation for joining the blocks
                            currVal = -1
                        elif self.boards[y2][x] == 0:
                            # move block to the right
                            print("Move Block " + str(x) + "," + str(y2) + " to " + str(x) + "," + str(y2-1))
                            self.boards[y2][x] = currVal
                            self.boards[(y2-1)][x] = 0
                            isMoved = True;
                            self.drawBlocks(x,y2,surf)
                            self.drawBlocks(x,(y2-1),surf)
                            time.sleep (15.0 / 1000.0)

        return isMoved;

    def drawBlocks(self, x, y, surf):
        block_image = pygame.image.load("images\\" + str(self.boards[y][x]) + ".png").convert()
        surf.blit(block_image, (10 + (60 * x), 10 + (60 * y)))
        pygame.display.flip()

    def gameOver(self):
        # loop through all blocks in board
        for y in range(0, self.y):
            for x in range(0, self.x):
                # check if any moves is available
                if self.boards[y][x] == 0:
                    return False
                else:
                    # check for the movement whether this block can be moved
                    # up, down, left, or right?
                    # move up can only be done if y is > 0
                    if (y > 0):
                        # try to look up
                        if self.boards[(y-1)][x] == self.boards[y][x]:
                            return False
                    # move down can only be done if y is < (self.y - 1)
                    if (y < (self.y - 1)):
                        # try to look down
                        if self.boards[(y+1)][x] == self.boards[y][x]:
                            return False
                    # move left can only be done if x is > 0
                    if (x > 0):
                        # try to look left
                        if self.boards[y][x-1] == self.boards[y][x]:
                            return False
                    # move right can only be done if x is < (self.x - 1)
                    if (x < (self.x - 1)):
                        # try to look right
                        if self.boards[y][x+1] == self.boards[y][x]:
                            return False;

        # otherwise
        return True;

# App Class
# This will act as the main class of the games which will handle
# screen render and keyboard input.
class App:
    windowWidth = 250
    windowHeight = 250

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

        # fill the window screen with brownies background
        self._display_surf.fill((187,173,160))

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
        # draw the game board
        self.board.printBoard(self._display_surf)
        
        pygame.display.flip()

        # print the current board
        print(self.board.boards);

    def on_cleanup(self):
        # quit the program
        pygame.quit()

    def on_execute(self):
        # check whether we can perform initialization on the pygame or not?
        if self.on_init() == False:
            self._running = False;

        # render the first image
        self.on_render()

        # check for keyboard input if the game is still running
        while(self._running):
            pygame.event.pump()

            events = pygame.event.get()
            for event in events:
                if (event.type == pygame.KEYDOWN):
                    keys = event.key
                
                    if (keys == pygame.K_RIGHT):
                        if (self.board.moveRight(self._display_surf)):
                            self.board.randomNumber()
                        
                    if (keys == pygame.K_LEFT):
                        if (self.board.moveLeft(self._display_surf)):
                            self.board.randomNumber()

                    if (keys == pygame.K_UP):
                        if (self.board.moveUp(self._display_surf)):
                            self.board.randomNumber()

                    if (keys == pygame.K_DOWN):
                        if (self.board.moveDown(self._display_surf)):
                            self.board.randomNumber()

                    if (keys == pygame.K_ESCAPE):
                        self._running = False

                    #self.on_loop()
                    self.on_render()

                    # check if game over or not?
                    if self.board.gameOver():
                        self._running = False;

            time.sleep (40.0 / 1000.0);

        self.on_cleanup()

# main procedure
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
