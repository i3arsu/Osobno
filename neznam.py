import sys
import matplotlib.pyplot as plt
import pygame
from time import sleep
from pygame.gfxdraw import aacircle as circ
from pygame.gfxdraw import filled_circle as fcirc
import numpy as np
from random import random

P1 = 3
P2 = 0.5
V1 = 2.0
V2 = (P1*V1)/P2

f = np.array([1,10,1.5])

plt.plot(f)

plt.show()
