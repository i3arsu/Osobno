import sys
import pygame
from pygame.gfxdraw import aacircle as circ
from pygame.gfxdraw import filled_circle as fcirc
import numpy as np
from time import sleep


#Rezolucija
Xsize = 1000
Ysize = 1000

#Konstante
g = 9.80
L = 200
theta = 1.2
tirkizna = [84,255,159]
purple = [131,111,255]

c1 = np.array([(L*np.sin(theta)+Xsize/2),L*np.cos(theta)])
c2 = np.array([540.0, 100+L])
v = 0
a=0


R = 20

#Poziv pygame
pygame.init()
#Otvaranje prozora
screen = pygame.display.set_mode((Xsize,Ysize))


#Pomak =


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

# def Kugla1():
#     pygame.draw.line(screen, purple, ((Xsize/2),100),((L*np.sin(theta)+Xsize/2),(L*np.cos(theta)+100)),2)
#     draw_circ(screen, c1, R, tirkizna)
#
# def Kugla1_pomak:
#
#
# def Kugle():
#     for i in range (1,5):
#         pygame.draw.rect(screen, purple, ((i*40)+339+(i),130, 2, 180), 0)
#         pygame.draw.circle(screen, tirkizna, ((i*40)+340+(i),320), 20, 0)
#
# def Kugla2(x2,y2):
#     pygame.draw.line(screen, purple, (x2,350),(x2,y2), 3)
#     # pygame.draw.circle(screen, white,(x,y), 20, 0)
#     draw_circ (screen, (x2,y2),20,tirkizna)
#
# def Kugla2_pokret(x2,y2):
#     theta = theta*np.cos((g/L)**(1/2)*t)
#
#     pygame.draw.line(screen, purple, (x2,350), [(L * np.sin(theta))+460,(L * np.cos(theta)+400)], 3)
#     # pygame.draw.circle(screen, white,(x,y), 20, 0)
#     draw_circ (screen, [(L * np.sin(theta))+x2,(L * np.cos(theta)+400)],20,tirkizna)

preklapanje = False
running = True
t=0

while running:

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    screen.fill(pygame.Color(0,0,0))


    #pygame.draw.line(screen, purple, ((Xsize/2),100),((L*np.sin(theta)+Xsize/2),(L*np.cos(theta)+100)),2)
    draw_circ(screen, c1, R, tirkizna)

    # a = -g*np.sin(theta)
    #
    # theta += v
    # v += a
    # c1 += v

    # Kugla1()
    # #Kugle()
    # #Kugla2(340,320)


    pygame.display.flip()
    sleep(1)

    #theta += v
    #v += akceleracija


    #
    # if not preklapanje and abs(c1[0]-c2[0])<2*R:
    #     preklapanje = True
    #     nova_v1 = sqrtE * np.cos(alpha)
    #     nova_v2 = sqrtE * np.sin(alpha)
    #     nova_v1, nova_v2 = sorted([nova_v1, nova_v2])
    #     if c1[0] >= c2[0]:
    #         v1[0] = nova_v2
    #         v2[0] = nova_v1
    #     else:
    #         v1[0] = nova_v1
    #         v2[0] = nova_v2
    #     print(v1[0], v2[0], v1[0]**2+v2[0]**2)
    # if preklapanje and  abs(c1[0]-c2[0])>=2*R:
    #     preklapanje = False
    # sleep(1/100)
    # t+=0.01
