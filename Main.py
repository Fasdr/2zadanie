import time
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, pi


h = 0.02
t = 0.01

nx = int(1/h)+1
nt = int(1/t)+1

u = np.zeros((nt, nx))
c = np.zeros((nt, nx))
ru = np.zeros((nt, nx))

for i in range(0, nx):
    for j in range(0, nt):
        ru[j][i] = sin(pi*i*h)+cos(2*pi*j*t)/2+2*pi*i*h-3.5*j*t

for i in range(0, nx):
    u[0][i] = sin(pi*i*h)+2*pi*i*h+1/2

for j in range(0, nt):
    u[j][0] = -3.5*j*t+cos(2*pi*j*t)/2

for i in range(0, nx):
    for j in range(0, nt):
        c[j][i] = (pi*sin(2*pi*j*t)+3.5)/(2*pi+pi*cos(pi*i*h))
starttime = time.time()

# for j in range(0, nt-1):
#     for i in range(1, nx-1):
#         u[j+1][i] = (u[j][i+1]+u[j][i-1])/2-t*c[j][i]*(u[j][i+1]-u[j][i-1])/(2*h)
#     u[j + 1][nx-1] = u[j][nx-1]*(1-t*c[j][nx-1]/h)+t*c[j][nx-1]/h*u[j][nx-2]

# for j in range(0, nt-1):
#     for i in range(1, nx-1):
#         u[j+1][i] = (u[j][i+1]+u[j][i-1])/2-t*c[j][i]*(u[j][i+1]-u[j][i-1])/(2*h)
#     u[j + 1][nx-1] = (u[j][nx-2]-u[j+1][nx-3]*(1/2-t*c[j+1][nx-2]/2/h))/(1/2+t*c[j+1][nx-2]/2/h)

# for j in range(0, nt-1):
#     for i in range(1, nx):
#         u[j + 1][i] = u[j][i] * (1 - t * c[j][i] / h) + t * c[j][i] / h * u[j][i - 1]

print(time.time()-starttime)

b = u-ru
c = -(u-ru)

print(b.max())
print(c.max())

# tt = np.arange(0, 1+t, t)
#
# xx = np.arange(0, 1+h, h)
#
# for i in range(0, 11):
#     plt.figure(figsize=(20, 10))
#     plt.subplot(1, 1,  1)
#     plt.plot(xx, u[i * int(0.1 / t)], 'bo')
#     plt.title('t = ' + str(i/10))
#     plt.xlabel('x')
#     plt.ylabel('Value')
#     plt.grid(True)
#     plt.subplot(1, 1,  1)
#     plt.plot(xx, ru[i * int(0.1 / t)], 'r+')
#     plt.grid(True)
#     plt.show()
#
# plt.figure(figsize=(20, 10))
# plt.subplot(1, 1,  1)
# plt.plot(tt, u[:, int(0.5 / h)], 'bo')
# plt.title('x = 0.5')
# plt.xlabel('t')
# plt.ylabel('Value')
# plt.grid(True)
# plt.subplot(1, 1,  1)
# plt.plot(tt, ru[:, int(0.5 / h)], 'r+')
# plt.grid(True)
# plt.show()
