import sys
import pygame
from pygame.gfxdraw import aacircle as circ
from pygame.gfxdraw import filled_circle as fcirc
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
from time import sleep

#Rezolucija
Xsize = 1000
Ysize = 800
#Konstante
g = 9.80
L = 200
l = 200*0.0264
m = 50
tirkizna = [84,255,159]
purple = [131,111,255]
theta = 1.2
br_kugli = 1

c1 = np.array([420,L])
c2 = np.array([460,L])
c3 = np.array([500,L])
c4 = np.array([540,L])
c5 = np.array([(L*np.sin(theta))+(Xsize/2)+80, L*np.cos(theta)])


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


def equations(y0, t):
	theta, x = y0
	f = [x, -(g/l) * np.sin(theta)]
	return f

def plot_results(time, theta1, theta2):
	   plt.plot(time, theta1[:,0])
	   plt.plot(time, theta2)
	   plt.show()





v = 0
a = 0
R = 20
Egp = m*g*L
T = 2*np.pi*(np.sqrt(L/g))

print(T)

#Graf
time = np.arange(0, 100.0, 0.025)
theta0 = theta
x0 = np.radians(0.0)
theta1 = odeint(equations, [theta0, x0],  time)
w = np.sqrt(g/l)
theta2 = [theta0 * np.cos(w*t) for t in time]

pygame.init()

screen = pygame.display.set_mode((Xsize,Ysize))

sudar1 = False
sudar2 = False
sudar3 = False
sudar4 = False

running = True
t = 0

while running and t<10:

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    screen.fill(pygame.Color(84,84,84))

    Kugla1()
    Kugla2()
    Kugla3()
    Kugla4()
    Kugla5()


    a = -(g/L)*np.sin(theta)
    v += a
    theta += v
    sleep(1/60)

    Ekin = (m*v**2)/2

    if sudar1 == False:
        c5 = np.array([(L*np.sin(theta))+(Xsize/2)+80, L*np.cos(theta)]) # Peta se mice
        c1 = np.array([420,L])
    if not sudar1 and c5[0]<=c4[0]+2*R: # Peta udara u cetvrtu
        sudar1 = True
        c4 = np.array([(L*np.sin(theta))+(Xsize/2)+40, L*np.cos(theta)])
        c5 = np.array([580,L])
    if sudar1 == True and c4[0] <= c3[0]+2*R: # Cetvrta udara u trecu
        sudar2 = True
        c3 = np.array([(L*np.sin(theta))+(Xsize/2), L*np.cos(theta)])
        c4 = np.array([540,L])
    if sudar2 == True and c3[0] <= c2[0]+2*R:
        sudar3 = True
        c2 = np.array([(L*np.sin(theta))+(Xsize/2)-40, L*np.cos(theta)])
        c3 = np.array([500,L])
    if sudar3 == True and c2[0] <= c1[0]+2*R:
        c1 = np.array([(L*np.sin(theta))+(Xsize/2)-80, L*np.cos(theta)])
        c2 = np.array([460,L])
        sudar1=False
        sudar2=False
        sudar3 = False

    t += 0.025
    pygame.display.flip()
plot_results(time, theta1, theta2)
