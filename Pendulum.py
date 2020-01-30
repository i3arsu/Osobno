import pygame
from pygame.gfxdraw import aacircle as circ
from pygame.gfxdraw import filled_circle as fcirc
import numpy as np
from time import sleep
import math
import random

#Rezolucija
Xsize = 960
Ysize = 960

#Konstante
g = 9.80
L = 150
PocetniKut = 1.2
white = [255, 255, 255]
red = [255, 0, 0]

#Poziv pygame
pygame.init()
#Otvaranje prozora
screen = pygame.display.set_mode((Xsize,Ysize))

#Funkcija za crtanje krugova
def draw_circ(screen, location, R, color):
    Sx = int(location[0])
    Sy = int(location[1])
    fcirc(screen, Sx, Sy, R, color)
    circ(screen, Sx, Sy, R, color)
    if Sx + R > Xsize:
        fcirc(screen, Sx-Xsize,  Sy, R, color)
        circ(screen, Sx-Xsize, Sy , R, color)
    if Sx - R < 0:
        fcirc(screen, Sx+Xsize, Sy , R, color)
        circ(screen, Sx+Xsize, Sy , R, color)


#Funkcija za pomicanje kugle
# def position(right, t):
#
#
#     theta = PocetniKut*np.cos((g/L)**(1/2)*t)
#
#     if right:
#         draw_circ (screen, [L * np.sin(theta),L * np.cos(theta)],20,white)  # Update position of bob
#         #rod.axis = [pend.pos[0], pend.pos[1], 0]  # Update rod's position
#     else:
#         pend2+=draw_circ (screen, [L * np.sin(theta) - 2, L * np.cos(theta)], 20, white)  # Update position of bob
#         #rod2.axis = [pend2.pos[0] + 2, pend2.pos[1], 0]  # Update rod's position
#
#     # Once the moving pendulum reaches theta = 0, switch to the other one
#     if theta <= 0:
#         return False  # Return
#     else:
#         return True
#

right = True
t = 0

while True:
    screen.fill(pygame.Color(0,0,0))

    theta = PocetniKut*np.cos((g/L)**(1/2)*t)

    if right:
        draw_circ (screen, [(L * np.sin(theta))+500,(L * np.cos(theta)+400)],20,white)  # Update position of bob
        #rod.axis = [pend.pos[0], pend.pos[1], 0]  # Update rod's position
    else:
        pend2+=draw_circ (screen, [L * np.sin(theta) - 2, L * np.cos(theta)], 20, white)  # Update position of bob
        #rod2.axis = [pend2.pos[0] + 2, pend2.pos[1], 0]  # Update rod's position

    # Once the moving pendulum reaches theta = 0, switch to the other one
    if theta <= 0:
        theta = False  # Return
    else:
        theta = True


    t += 0.01
    pygame.display.flip()
