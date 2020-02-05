import sys
import pygame
from pygame.gfxdraw import aacircle as circ
from pygame.gfxdraw import filled_circle as fcirc
import numpy as np
from time import sleep

#Rezolucija
Xsize = 1000
Ysize = 800
#Konstante
g = 9.80
L = 200
tirkizna = [84,255,159]
purple = [131,111,255]
theta = 1.2

c1 = np.array([420,L])
c2 = np.array([460,L])
c3 = np.array([500,L])
c4 = np.array([540,L])
c5 = np.array([(L*np.sin(theta))+(Xsize/2)+80, L*np.cos(theta)])
print(L*np.sin(theta))


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




def Kugla1():
    pygame.draw.line(screen, purple, ((Xsize/2)-80, 0), c1, 2)
    draw_circ(screen, c1, 20, tirkizna)

def Kugla2():
    pygame.draw.line(screen, purple, ((Xsize/2)-40, 0), c2, 2)
    draw_circ(screen, c2, 20, tirkizna)

def Kugla3():
    pygame.draw.line(screen, purple, ((Xsize/2), 0), c3, 2)
    draw_circ(screen, c3, 20, tirkizna)

def Kugla4():
    pygame.draw.line(screen, purple, ((Xsize/2)+40, 0), c4, 2)
    draw_circ(screen, c4, 20, tirkizna)

def Kugla5():
    pygame.draw.line(screen, purple, ((Xsize/2)+80, 0), c5, 2)
    draw_circ(screen, c5, 20, tirkizna)


# Napraviti Kuglu 2 i prenjeti brzinu pri udarcu na nju


v=0
a=0
R = 20


pygame.init()

screen = pygame.display.set_mode((Xsize,Ysize))

sudar1 = False
sudar2 = False
running = True

while running:

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    screen.fill(pygame.Color(84,84,84))

    Kugla1()
    Kugla2()
    Kugla3()
    Kugla4()
    Kugla5()


    a = -0.01*np.sin(theta)
    v += a
    theta += v
    #c5 = np.array([(L*np.sin(theta))+(Xsize/2)+80, L*np.cos(theta)])
    sleep(1/30)

    if sudar1 == False:
        c5 = np.array([(L*np.sin(theta))+(Xsize/2)+80, L*np.cos(theta)])
        sudar2 = True
        c1 = np.array([420,L])

    if not sudar1 and c5[0]<=(c4[0]+R*2):
        sudar1 = True
        sudar2 = False
        c5 = np.array([580,L])

    if sudar1 and c5[0]>=c4[0]+2*R:
        sudar1 = False

    if sudar2 == False:
        c1 = np.array([(L*np.sin(theta))+(Xsize/2)-80, L*np.cos(theta)])


    pygame.display.flip()
