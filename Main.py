import matplotlib.pyplot as plt
import numpy as np
from math import exp, sin, cos, pi

h = 0.1
t = 0.1

nx = int(1/h)+1
nt = int(1/t)+1

u = np.zeros((nt, nx))
c = np.zeros((nt, nx))
ru = np.zeros((nt, nx))

for i in range(0, nx):
    for j in range(0, nt):
        ru[j][i] = -sin(pi*i*h)-cos(2*pi*j*t)/2+2*pi*i*h-3.5*j*t


