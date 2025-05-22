import pygame
import math
from sys import exit
import random
import numpy as np
import RRCL
from random import randint


pygame.init()


screen = pygame.display.set_mode((800,600))
screenSize = screen.get_size()

screenCenter = [screenSize[0]/2, screenSize[1]/2]


colors = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
#colors = ['orange', 'red', 'red', 'red', 'white', 'white', 'orange', 'green', 'green', 'red', 'blue', 'blue', 'blue', 'yellow', 'blue', 'orange', 'orange', 'green', 'blue', 'orange', 'white', 'white', 'green', 'green', 'green', 'white', 'red', 'green', 'yellow', 'red', 'blue', 'blue', 'yellow', 'blue', 'green', 'blue', 'orange', 'red', 'yellow', 'white', 'red', 'green', 'white', 'yellow', 'white', 'yellow', 'yellow', 'white', 'orange', 'orange', 'orange', 'yellow', 'red', 'yellow']
#colors = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'yellow', 'blue', 'red', 'orange', 'yellow', 'green', 'yellow', 'yellow', 'red', 'green', 'green', 'green', 'blue', 'green', 'yellow', 'orange', 'red', 'blue', 'orange', 'orange', 'green', 'orange', 'blue', 'red', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'green', 'red', 'yellow', 'yellow', 'red', 'yellow', 'orange', 'orange', 'orange', 'green', 'orange', 'yellow', 'green', 'blue', 'blue']

angle = [0,0]

while True:
    mouse = False
    for event in pygame.event.get():     
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            print(colors)
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                RRCL.rotateSide(colors, 0)
            if event.key == pygame.K_1:
                RRCL.rotateSide(colors, 1)
            if event.key == pygame.K_2:
                RRCL.rotateSide(colors, 2)
            if event.key == pygame.K_3:
                RRCL.rotateSide(colors, 3)
            if event.key == pygame.K_4:
                RRCL.rotateSide(colors, 4)
            if event.key == pygame.K_5:
                RRCL.rotateSide(colors, 5)

                          
    screen.fill((0,0,0))


    




    angle = RRCL.detectRotations(pygame.mouse.get_pressed(), pygame.mouse.get_rel() ,angle)




    colors = RRCL.renderCube(colors, angle, screen, mouse, pygame.mouse.get_pos(), True)
   

    pygame.display.update()
