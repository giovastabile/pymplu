"""
PyMPLU init
"""
import matplotlib.pyplot as plt
__all__ = ["pymplu"]
plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "serif"
SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

from .pymplu import *

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title