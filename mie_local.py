# ======== Mie theory analysis codes ======
# Mie theory optical cross sections from a multi-layered spherical particle
# Reference: Moroz (2005)
#   http://dx.doi.org/10.1016/j.aop.2004.07.002  
#   http://www.wave-scattering.com/moroz.html


# ======== Header ========
# -------- Import modules --------
# math 
from math import *
from cmath import *

# directory access
import os

# Numerical Python with multidimensional arrays
import numpy as np

# Scientific python for bessel functions
import scipy as sp
from scipy.special import *

# Scientific python for interpolation
import scipy.interpolate as interpolate

# basic Mie theory functions
from mie import *

# refractive index library
from refractive_index_library import *

# -------- Fundamental constants --------
import scipy.constants as SI
AvogadroN = SI.N_A # 1/mol, Avogadro's number
cumfs = SI.c*1e-15*1e6 # micron/fs, vacuum speed of light
cnmfs = SI.c*1e-15*1e9 # nm/fs, vacuum speed of light
heVfs = SI.codata.value('Planck constant in eV s')*1e15 # eV*fs, Planck's constant
hbareVfs = heVfs/(2*pi) # eV*fs, h-bar, reduced Planck's constant
eMass0eVnmfs = SI.codata.value('electron mass energy equivalent in MeV')*1e6/(cnmfs*cnmfs) # eV/c^2 (c in nm/fs) = eV*fs^2/nm^2, electron mass
eps0enmV = 1/(2*SI.alpha*heVfs*cnmfs) # e^2/(eV*nm), permittivity of free space


# ======== Function definitions ========
# -------- Check to see if functions are loaded --------
def printCheck():
    print("  ... local Mie functions loaded")
    return

# -------- Analysis-specific codes --------

# For checking lmax necessary for convergence
def CextRelDipEMList(CextEMList):
    return [CextEMList[0][-1]/CextEMList[0][0], CextEMList[1][-1]/CextEMList[1][0]]

# Au NP in water, list of extinction cross sections by polarization and multipole
def CextEMListAuH2O(lmax, rCorenm, wl0nm):
    nmed = nH2O(wl0nm)
    return [CextEList(lmax, [nAuSc(wl0nm,rCorenm*4/3),nmed], [rCorenm], 2*pi/wl0nm),
     CextMList(lmax, [nAuSc(wl0nm,rCorenm*4/3),nmed], [rCorenm], 2*pi/wl0nm)]
# Total extinction cross section
def CextAuH2O(lmax, rCorenm, wl0nm):
    nmed = nH2O(wl0nm)
    return Cext(lmax, [nAuSc(wl0nm,rCorenm*4/3),nmed], [rCorenm], 2*pi/wl0nm)

# Au core-shell NP with swollen PNIPAM shell in water
# List of extinction cross sections by polarization and multipole
def CextEMListAuGelH2O(lmax, rCorenm, rShellnm, wl0nm):
    nmed = nH2O(wl0nm)
    nShell = nmed + 0.042
    return [CextEList(lmax, [nAuSc(wl0nm,rCorenm*4/3),nShell,nmed], [rCorenm,rShellnm], 2*pi/wl0nm),
     CextMList(lmax, [nAuSc(wl0nm,rCorenm*4/3),nShell,nmed], [rCorenm,rShellnm], 2*pi/wl0nm)]
# Total extinction cross section
def CextAuGelH2O(lmax, rCorenm, rShellnm, wl0nm):
    nmed = nH2O(wl0nm)
    nShell = nmed + 0.042
    return Cext(lmax, [nAuSc(wl0nm,rCorenm*4/3),nShell,nmed], [rCorenm,rShellnm], 2*pi/wl0nm)