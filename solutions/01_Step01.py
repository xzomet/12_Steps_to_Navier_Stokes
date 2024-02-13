#!/usr/bin/env python
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt


nx = 21 # # of points in space, nx-1 slices
nt = 50 # # of points in time
dt = 0.01 # time interval (step in time)
dx = 2 / (nx-1) # space interval (size of a slice)
c = 1 # wave length, const.


x = np.linspace(0, 2, nx) # point coords. in space
u = np.ones(nx) # initial array to store u values


# rearrange the u array for the initial conditions
# I.C.s: u = 2 @ 0.5 <= x <= 1
#        u = 1 @ everywhere else in (0, 2)
# B.C.s: u = 1 @ x = 0, x = 2
for i in range(nx):
    if 0.5 <= x[i] <= 1:
        u[i] = 2
    else:
        u[i] = 1
print(u)
plt.plot(x,u)
plt.show()

# Calculate u for nt time steps and show the nth u array.
for t in range(nt):
    # copy the old u values to a temp. un array
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])


print(u)
plt.plot(np.linspace(0, 2, nx), u);
plt.show()
