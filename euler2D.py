# euler2D.py
# example script to integrate two two dimensional
# first order differential equations

# import modules here
# ============================================ #
import numpy as np
import matplotlib.pyplot as plt
from eulers import *

# ============================================ #

# define derivatives here
# ============================================ #
def xprime(x, y):
    return y + y**2

def yprime(x, y):
    return -x + (y/5) - (x*y) + ((6/5)*(y**2))
# ============================================ #
# call Euler2D function to calculate time, x points and y points
time, xpts, ypts = Euler2D(xprime, yprime, 0, 1, 1, 0.001, 10000)

# make plot
# ============================================ #
fig, axs = plt.subplots(3, figsize=(7, 10))
plt.subplots_adjust(hspace=0.2)

axs[0].plot(time, xpts, color='black')
axs[0].tick_params(axis='both', direction='in', which='both', top=True, right=True)
plt.text(0.5, -0.15, r't', transform=axs[0].transAxes, ha='center')
plt.text(-0.1, 0.5, 'x(t)', transform=axs[0].transAxes, va='center', rotation='vertical')

axs[1].plot(time, ypts, color='black')
axs[1].tick_params(axis='both', direction='in', which='both', top=True, right=True)
plt.text(0.5, -0.15, r't', transform=axs[1].transAxes, ha='center')
plt.text(-0.1, 0.5, 'y(t)', transform=axs[1].transAxes, va='center', rotation='vertical')

axs[2].plot(xpts, ypts, color='black')
axs[2].tick_params(axis='both', direction='in', which='both', top=True, right=True)
plt.text(0.5, -0.15, r'x(t)', transform=axs[2].transAxes, ha='center')
plt.text(-0.1, 0.5, r'y(t)', transform=axs[2].transAxes, va='center', rotation='vertical')
# ============================================ #