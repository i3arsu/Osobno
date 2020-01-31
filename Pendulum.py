import sys
import pygame
from pygame.gfxdraw import aacircle as circ
from pygame.gfxdraw import filled_circle as fcirc
import numpy as np
from time import sleep
import random

#Rezolucija
Xsize = 1000
Ysize = 960

#Konstante
g = 9.80
L = 100
PocetniKut = 1.2
tirkizna = [84,255,159]
purple = [131,111,255]

#Poziv pygame
pygame.init()
#Otvaranje prozora
screen = pygame.display.set_mode((Xsize,Ysize))


# Funkcija za crtanje krugova
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

def Kugla2(x,y):
    pygame.draw.line(screen, purple, (x,350),(x,y), 3)
    # pygame.draw.circle(screen, white,(x,y), 20, 0)
    draw_circ (screen, (x,y),20,tirkizna)

def Kugla2_pokret(x,y):
    theta = PocetniKut*np.cos((g/L)**(1/2)*t)

    pygame.draw.line(screen, purple, (x,350), [(L * np.sin(theta))+460,(L * np.cos(theta)+400)], 3)
    # pygame.draw.circle(screen, white,(x,y), 20, 0)
    draw_circ (screen, [(L * np.sin(theta))+x,(L * np.cos(theta)+400)],20,tirkizna)
#
#
#
# def first_marble(x_, y_):
#     if (x_>340):
#         x_ = 340
#     if (y_>320):
#         y_ = 320
#     pygame.draw.line(screen, red, (340,130), (x_,y_), 2)
#     pygame.draw.circle(screen, white, (x_, y_), 20, 0)
#
# def marble():
#         pygame.draw.rect(screen, red, ((i*40)+339+(i),130, 2, 180), 0)
#         pygame.draw.circle(screen, white, ((i*40)+340+(i),320), 20, 0)
#
# def end_marble(x, y):
#     if (x<544):
#         x = 544
#         y = 320
#     if (y>322):
#         y = 320
#     pygame.draw.line(screen, red, (544,130), (x,y), 2)
#     pygame.draw.circle(screen, white, (x, y), 20, 0)


right = True
t = 0
# clicked = 0

Kugla2(460,550)

while True:
    screen.fill(pygame.Color(84,84,84))

    theta = PocetniKut*np.cos((g/L)**(1/2)*t)


    #Kugla2(460,550)

    pygame.draw.line(screen,[255,250,250],(350,350),(600,350),5)

    if right:
        pygame.draw.line(screen, purple, (500,350), [(L * np.sin(theta))+500,(L * np.cos(theta)+400)], 3)
        draw_circ (screen, [(L * np.sin(theta))+500,(L * np.cos(theta)+400)],20,tirkizna)
        Kugla2(460,(400+L))  # Stacionarna kugla 2

    else:
        Kugla2_pokret(460,550)
        pygame.draw.line(screen, purple, (500,350), (500,(400+L)), 3)
        draw_circ (screen, (500,(400+L)),20,tirkizna)


    # Kad pendulum dode do theta = 0 prebaci se na lijevi
    if theta <= 0:
        right = False  # Return
    else:
        right = True

    t += 0.01
    pygame.display.flip()
