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
Ysize = 400
#Konstante
g = 9.80
L = 200
l = 200*0.0264
m = 50
R = 20

tirkizna = [84,255,159]
purple = [131,111,255]
theta0 = 1.2
br_kugli = 1
kugla = []
x0 = 420
for i in range(5):
    kugla.append(np.array([x0+i*40,L]))

def draw_circ(screen, location, R, color):
    Sx = int(location[0])
    Sy = int(location[1])
    fcirc(screen, Sx, Sy, R, color)
    circ(screen, Sx, Sy, R, color)

def Kugla(screen, kugla, x):
    pygame.draw.line(screen, purple, ((Xsize/2)-x, 0), kugla, 2)
    draw_circ(screen, kugla, R, tirkizna)

def formule(y0, t):
    theta0, x = y0
    f = [x, -(g/l) * np.sin(theta0)]
    return f

def plot_results(time, theta1, theta2):
       plt.plot(time, theta1[:,0])
       plt.plot(time, theta2)
       plt.xlabel('Vrijeme (s)')
       plt.ylabel('Kut (Radijani)')
       plt.legend(['Nelinearno', 'Linearno'], loc='top right')
       plt.show()


Egp = m*g*l
T = 2*np.pi*(np.sqrt(l/g))

print(T)

#Graf
time = np.arange(0, 10, 0.025)

x0 = np.radians(0.0)
theta1 = odeint(formule, [theta0, x0],  time)
w = np.sqrt(g/l)
theta2 = [theta0 * np.cos(w*t) for t in time]

running = True
t = 0

dt = 0.025

n = int(input("Koliko kuglica želiš pomaknuti? "))

pygame.init()
screen = pygame.display.set_mode((Xsize,Ysize))

dx = 80
for i in range(n):
    kugla[-(i+1)] = np.array([(L*np.sin(theta0))+(Xsize/2)+dx, L*np.cos(theta0)])
    dx -= 40

while running and t<10:
    theta = theta0 * np.cos(w*t)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    screen.fill(pygame.Color(84,84,84))
    x1 = 80
    for i in range(5):
        Kugla(screen, kugla[i], x1)
        x1 -= 40

    if theta >= 0:
        dx = 80
        j = 0
        for i in range(n):
            kugla[j] = np.array([420 + j*40, L])
            kugla[-(i+1)] = np.array([(L*np.sin(theta))+(Xsize/2)+dx, L*np.cos(theta)])
            dx -= 40
            if j < 5-n:
                j += 1
    else:
        dx = -80
        j = 0
        for i in range(n):
            kugla[-(j+1)] = np.array([580 - j*40, L])
            kugla[i] = np.array([(L*np.sin(theta))+(Xsize/2)+dx, L*np.cos(theta)])
            dx += 40
            if j < 5-n:
                j+=1

    sleep(0.025)

    t += dt
    pygame.display.flip()
plot_results(time, theta1, theta2)
