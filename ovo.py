import sys
import pygame
from pygame.gfxdraw import aacircle as circ
from pygame.gfxdraw import filled_circle as fcirc
import numpy as np
from time import sleep
import matplotlib.pyplot as plt



#Rezolucija
Xsize = 1000
Ysize = 960

#Konstante
g = 9.80
m = 50
L = 100 # pixeli
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



right = True
t = 0
running = True

v1=0

A = (L* 0.0264)-((L* 0.0264)*np.cos(PocetniKut)) # Max vrijednost
#T = (2*np.pi())*np.sqrt((L*0.0264)/g) # Amplituda




Kugla2(460,550)

while running:

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    screen.fill(pygame.Color(84,84,84))

    theta = PocetniKut*np.cos((g/L)**(1/2)*t)
    A = (L* 0.0264)-((L* 0.0264)*np.cos(theta))
    print(theta)
    sleep(0.01)



    #Kugla2(460,550)

    pygame.draw.line(screen,[255,250,250],(350,350),(600,350),5)

    if right:
        pygame.draw.line(screen, purple, (500,350), [(L * np.sin(theta))+500,(L * np.cos(theta)+400)], 3)
        draw_circ (screen, [(L * np.sin(theta))+500,(L * np.cos(theta)+400)],20,tirkizna)
        Kugla2(460,(400+L))  # Stacionarna kugla 2
        v1 = 0
        v1 += (np.sqrt(g/(L*0.0264)*A*np.sin(theta)))
        v2=v1
        Eukup = m*g*A+((m*(v1**2))/2)
    #    print(Eukup,"  ",m*g*A,"  ",(m*v1**2)/2)



    else:
        Kugla2_pokret(460,550)
        pygame.draw.line(screen, purple, (500,350), (500,(400+L)), 3)
        draw_circ (screen, (500,(400+L)),20,tirkizna)
        v2-= (np.sqrt(g/(L*0.0264)*A*np.sin(theta)))
        Eukup = m*g*A+((m*(v2**2))/2)
    #    print(Eukup,"  ",m*g*A,"  ",(m*v2**2)/2)





    # Kad pendulum dode do theta = 0 prebaci se na lijevi
    if theta <= 0:
        right = False  # Return
    else:
        right = True

    t += 0.01


    pygame.display.flip()
    # sleep(60)




xos = np.array([0,t,0,1])
yos = np.sin(xos)
plt.plot(xos,yos)
plt.show()

# kolicina_gibanja_nakon = m1*v1 + m2*v2
# kolicina_gibanja_prije
