## ======== Refractive index library ======== ##
# load refractive index from data and convert to functions of wavelength (nm)
# includes confinement effects for metals
# includes semi-analytic models for many solvents

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

# Scientific python for interpolations
import scipy.interpolate as interpolate

# -------- Fundamental constants --------
import scipy.constants as SI
AvogadroN = SI.N_A # 1/mol, Avogadro's number
cumfs = SI.c*1e-15*1e6 # micron/fs, vacuum speed of light
cnmfs = SI.c*1e-15*1e9 # nm/fs, vacuum speed of light
heVfs = SI.codata.value('Planck constant in eV s')*1e15 # eV*fs, Planck's constant
hbareVfs = heVfs/(2*pi) # eV*fs, h-bar, reduced Planck's constant
eMass0eVnmfs = SI.codata.value('electron mass energy equivalent in MeV')*1e6/(cnmfs*cnmfs) # eV/c^2 (c in nm/fs) = eV*fs^2/nm^2, electron mass
eps0enmV = 1/(2*SI.alpha*heVfs*cnmfs) # e^2/(eV*nm), permittivity of free space


# -------- Check to see if functions are loaded --------
def printCheck():
    print("  ... refractive index functions loaded:")
    print("       Au, Ag, SiO2, ITO, ZnO, H2O, ")
    print("       ethanol, CS2, benzene, toluene, ")
    print("       chloroform, methanol, butanol, ")
    print("       propanol")
    return


# -------- Metals --------

# Au: [188,1935] nm
# Johnson & Christy (1972)
nArray = np.genfromtxt("optical-data/Johnson-Au.csv", delimiter=",")
# Interpolation function
nAuRe = interpolate.interp1d(1000*nArray[:,0], nArray[...,1], kind="cubic")
nAuIm = interpolate.interp1d(1000*nArray[:,0], nArray[...,2], kind="cubic")
def nAu (wl0nm):
    return nAuRe(wl0nm) + 1j*nAuIm(wl0nm)
# Include electron scattering for confined geometries (thin shells, small particles)
# For spheres, lsc = (4/3)*Radius
# For shells, lsc = thickness
def nAuSc (wl0nm, lscnm): 
    nMetal = nAu(wl0nm) # refractive index of Au
    ck0fs = cnmfs*(2*pi/wl0nm) # rad/fs, light angular frequency
    nenm3 = 59 # conduction electron number density for Au and Ag /nm^3
    vfnmfs = (hbareVfs/eMass0eVnmfs)*pow(3.0*pi*pi*nenm3,1/3) # nm/fs, mean speed
    omegaPfs = pow(nenm3/(eMass0eVnmfs*eps0enmV),1/2) # rad/fs, bulk plasma frequency
    neff = sqrt((nMetal*nMetal) + 1j*(pow(omegaPfs,2)*vfnmfs/(pow(ck0fs,3)*lscnm)))
    return neff

# Ag: [188,1935] nm
# Johnson & Christy (1972)
nAgArray = np.genfromtxt("optical-data/Johnson-Ag.csv", delimiter=",")
# Interpolation function
nAgRe = interpolate.interp1d(1000*nAgArray[:,0], nAgArray[...,1], kind="cubic")
nAgIm = interpolate.interp1d(1000*nAgArray[:,0], nAgArray[...,2], kind="cubic")
def nAg (wl0nm):
    return nAgRe(wl0nm) + 1j*nAgIm(wl0nm)
# Include electron scattering for confined geometries (thin shells, small particles)
# For spheres, lsc = (4/3)*Radius
# For shells, lsc = thickness
def nAgSc (wl0nm, lscnm): 
    nMetal = nAg(wl0nm) # refractive index of Ag
    ck0fs = cnmfs*(2*pi/wl0nm) # rad/fs, light angular frequency
    nenm3 = 59 # conduction electron number density for Au and Ag /nm^3
    vfnmfs = (hbareVfs/eMass0eVnmfs)*pow(3.0*pi*pi*nenm3,1/3) # nm/fs, mean speed
    omegaPfs = pow(nenm3/(eMass0eVnmfs*eps0enmV),1/2) # rad/fs, bulk plasma frequency
    neff = sqrt((nMetal*nMetal) + 1j*(pow(omegaPfs,2)*vfnmfs/(pow(ck0fs,3)*lscnm)))
    return neff


# -------- Solid dieletrics (substrates) --------

# Silica [252,1250] nm
# Gao (2013)
nSiO2Array = np.genfromtxt("optical-data/SiO2-Gao-nk.txt", delimiter="\t")
# Interpolation function
nSiO2Re = interpolate.interp1d(1000*nSiO2Array[:,0], nSiO2Array[...,1], kind="cubic")
nSiO2Im = interpolate.interp1d(1000*nSiO2Array[:,0], nSiO2Array[...,2], kind="cubic")
def nSiO2 (wl0nm):
    return nSiO2Re(wl0nm) + 1j*nSiO2Im(wl0nm)

# ITO [252,1000] nm
# Koenig (2014)
nITOArray = np.genfromtxt("optical-data/ITO.txt", delimiter="\t")
# Interpolation function
nITORe = interpolate.interp1d(1000*nITOArray[:,0], nITOArray[...,1], kind="cubic")
nITOIm = interpolate.interp1d(1000*nITOArray[:,0], nITOArray[...,2], kind="cubic")
def nITO (wl0nm):
    return nITORe(wl0nm) + 1j*nITOIm(wl0nm)

# ZnO [450,800] nm
# Hu 1997
def nZnO (wl0nm):
    A1 = 1.9281
    A2 = -1.1157e-5
    A3 = 5.9696e-3
    wlum = wl0nm*1e-3
    return A1 + A2/(wlum*wlum) + A3/(pow(wlum,4))


# -------- Liquids & solvents --------

# Water [200,1100] nm
# Daimon 2007
def nH2O (wl0nm):
    A1 = 5.684027565e-1
    A2 = 1.726177391e-1
    A3 = 2.086189578e-2
    A4 = 1.130748688e-1
    wlum = wl0nm*1e-3
    wl1um2 = 5.101829712e-3
    wl2um2 = 1.821153936e-2
    wl3um2 = 2.620722293e-2
    wl4um2 = 1.06979271e1
    return sqrt(1 + 
                A1*(wlum*wlum)/(wlum*wlum-wl1um2) + 
                A2*(wlum*wlum)/(wlum*wlum-wl2um2) + 
                A3*(wlum*wlum)/(wlum*wlum-wl3um2) + 
                A4*(wlum*wlum)/(wlum*wlum-wl4um2)
                )

# Ethanol [500,1600] nm
# Kedenburg (2012)
def nEtOH (wl0nm):
    C0 = 1.83347
    C1 = 0.00648
    C2 = 0.00031
    C3 = 0.
    C4 = 0.
    C5 = -0.00352
    wlum = wl0nm*1e-3
    return sqrt(C0 + 
                C1/pow(wlum,2) + 
                C2/pow(wlum,4) + 
                C3/pow(wlum,6) + 
                C4/pow(wlum,8) + 
                C5*pow(wlum,2)
               )


# Carbon disulfide [300,2500] nm
# Samoc 2003
def nCS2 (wl0nm):
    C0 = 1.582445
    C1 = 13.7372e3
    C2 = 10.0243e8
    C3 = -15.6572e13
    C4 = 1.8294e18
    C5 = -3.2117e-10
    return sqrt(C0 + 
                C1/pow(wl0nm,2) + 
                C2/pow(wl0nm,4) + 
                C3/pow(wl0nm,6) + 
                C4/pow(wl0nm,8) + 
                C5*pow(wl0nm,2)
               )

# Benzene [300,2500] nm
# Samoc 2003
def nBenz (wl0nm):
    C0 = 1.473644
    C1 = 11.26920e3
    C2 = -9.2034e8
    C3 = 12.4302e13
    C4 = -3.9224e18
    C5 = 4.8623e-10
    return sqrt(C0 + 
                C1/pow(wl0nm,2) + 
                C2/pow(wl0nm,4) + 
                C3/pow(wl0nm,6) + 
                C4/pow(wl0nm,8) + 
                C5*pow(wl0nm,2)
               )

# Toluene [300,2500] nm
# Samoc 2003
def nTolu (wl0nm):
    C0 = 1.474775
    C1 = 6.99031e3
    C2 = 2.1776e8
    C3 = 0.
    C4 = 0.
    C5 = 0.
    return sqrt(C0 + 
                C1/pow(wl0nm,2) + 
                C2/pow(wl0nm,4) + 
                C3/pow(wl0nm,6) + 
                C4/pow(wl0nm,8) + 
                C5*pow(wl0nm,2)
               )

# Chloroform [300,2500] nm
# Samoc 2003
def nChloro (wl0nm):
    C0 = 1.431364
    C1 = 5.63241e3
    C2 = -2.0805e8
    C3 = 1.2613e13
    C4 = 0.
    C5 = 0.
    return sqrt(C0 + 
                C1/pow(wl0nm,2) + 
                C2/pow(wl0nm,4) + 
                C3/pow(wl0nm,6) + 
                C4/pow(wl0nm,8) + 
                C5*pow(wl0nm,2)
               )

# Methanol [400,1600] nm
# Moutzouris 20133
def nMeOH (wl0nm):
    wlum = 1e-3*wl0nm
    A0 = 1.745946239
    A1 = -0.005362181
    A2 = 0.004656355
    A3 = 0.0044714
    A4 = -0.000015087
    return sqrt(A0 + 
                A1*pow(wlum,2) + 
                A2/pow(wlum,2) + 
                A3/pow(wlum,4) + 
                A4/pow(wlum,6)
               )

# Butanol (1) [400,1600] nm
# Moutzouris 20133
def nBuOH (wl0nm):
    wlum = 1e-3*wl0nm
    A0 = 1.917816501
    A1 = -0.00115077
    A2 = 0.01373734
    A3 = -0.00194084
    A4 = 0.000254077
    return sqrt(A0 + 
                A1*pow(wlum,2) + 
                A2/pow(wlum,2) + 
                A3/pow(wlum,4) + 
                A4/pow(wlum,6)
               )

# Propanol (1) [400,1600] nm
# Moutzouris 20133
def nPrOH (wl0nm):
    wlum = 1e-3*wl0nm
    A0 = 1.89400242
    A1 = -0.003349425
    A2 = 0.004418653
    A3 = 0.00108023
    A4 = -0.000067337
    return sqrt(A0 + 
                A1*pow(wlum,2) + 
                A2/pow(wlum,2) + 
                A3/pow(wlum,4) + 
                A4/pow(wlum,6)
               )

