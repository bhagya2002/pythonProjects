# classic snake game

# imports
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

# cube object (each cube of snake)
class cube(object):
    rows = 0
    w = 0
    def __init__(self,start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

# snake object
class snake(object):
    def __init__(self,color, pos):
        pass
    def move(self):
        pass
    def reset(self, pos):
        pass
    def addCube(self):
        pass
    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    pass

def redrawWindow(surface):
    pass

def randomSnack(rows, items):
    pass

def messageBox(subject, content):
    pass


# game loop
def main():
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height)) # create a canvas to play on

    s = snake((255, 0, 0), (10, 10)) # create the red snake at position center

    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50) # delay of 50ms each update
        clock.tick(10) # 10 fps

        redrawWindow(win)
    pass


cube.rows = rows
cube.w = w

main()
