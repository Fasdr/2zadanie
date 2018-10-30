import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos

h = 0.1
t = 0.1

nx = int(1/h)+1
nt = int(1/t)+1

u = np.zeros((nt, nx))
c = np.zeros((nt, nx))
ru = np.zeros((nt, nx))




