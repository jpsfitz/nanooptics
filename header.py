## ======== Header ======== ##
# load python modules, 
# set fundamental constants,
# set basic directories,  
# load graphics options, 
# load refractive index library,

# -------- Import modules --------
print("Loading import modules ...")

# math 
from math import *
from cmath import *

# directory access, system variables
global os, sys, types
import os, sys, types

# time monitoring
global time, datetime
import time
import datetime

# parallel processing
global ipp
import ipyparallel as ipp

# Numerical Python with multidimensional arrays
global np
import numpy as np

# Scientific python for bessel functions
global sp
import scipy as sp
from scipy.special import *

# Scientific python 
global interpolate, signal
import scipy.interpolate as interpolate
import scipy.signal as signal

# python 2D plotting library
global plt, pylab, cm, LogNorm
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.pylab as pylab
from matplotlib.colors import LogNorm

# peak detection
# https://bitbucket.org/lucashnegri/peakutils
global peakutils
import peakutils


# -------- Fundamental constants --------
global SI
import scipy.constants as SI
global AvogadroN, cumfs, cnmfs, heVfs, hbareVfs, eMass0eVnmfs, eps0enmV
AvogadroN = SI.N_A # 1/mol, Avogadro's number
cumfs = SI.c*1e-15*1e6 # micron/fs, vacuum speed of light
cnmfs = SI.c*1e-15*1e9 # nm/fs, vacuum speed of light
heVfs = SI.codata.value('Planck constant in eV s')*1e15 # eV*fs, Planck's constant
hbareVfs = heVfs/(2*pi) # eV*fs, h-bar, reduced Planck's constant
eMass0eVnmfs = SI.codata.value('electron mass energy equivalent in MeV')*1e6/(cnmfs*cnmfs) # eV/c^2 (c in nm/fs) = eV*fs^2/nm^2, electron mass
eps0enmV = 1/(2*SI.alpha*heVfs*cnmfs) # e^2/(eV*nm), permittivity of free space


# -------- Local modules --------
print("Loading analysis codes ... ")

# Optical data
global ri
import refractive_index_library as ri
ri.printCheck()

# Mie theory codes
global mie, mie_local
import mie # General
mie.printCheck()
import mie_local # Analysis-specific
mie_local.printCheck()


# -------- Announce ready --------
print("Ready player one.")