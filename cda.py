# ======== CDA analysis codes ======
# The coupled dipole approximation (CDA)
# References: 
#  - Semi-analytic model: Zou, Janel, Schatz (2003)  
#   http://dx.doi.org/10.1063/1.1760740 
#  - The discrete dipole approximation (DDA): Draine (1988)
#   http://dx.doi.org/10.1086/166795


# ======== Header ========
# -------- Import modules --------
# math 
from math import *
from cmath import *

# Numerical Python with multidimensional arrays
import numpy as np

# ======== Function definitions ========
# -------- Check to see if functions are loaded --------
def printCheck():
    print("  ... CDA functions loaded")
    return


# -------- Lattice sums --------
# Identical dipoles, 2D, normal incidence, simplifed geometry lists
# Scalar, in-plane
def latticeSumS0(RmagList, NList, k):
    
    def S (r, n):
        return ( np.exp(1j*k*r)/r**3 )*( (k**2)*(r**2) + (1 - 1j*k*r))*(n/2)
    
    Stot = 0
    length = len(RmagList)
    
    for i in range(length):
        R = RmagList[i]
        N = NList[i]
        Stot += S(R,N)
    
    return Stot

# Scalar, out-of-plane
def latticeSumS0z(RmagList, NList, k):
    
    def S (r, n):
        return ( np.exp(1j*k*r)/r**3 )*( (k**2)*(r**2) - (1 - 1j*k*r))*(n)
    
    Stot = 0
    length = len(RmagList)
    
    for i in range(length):
        R = RmagList[i]
        N = NList[i]
        Stot += S(R,N)
    
    return Stot

# Matrix 
def latticeSumS0Mat(RmagList, NList, k):
    Sxy = latticeSumS0(RmagList, NList, k)
    Sz = latticeSumS0z(RmagList, NList, k)
    SMatTot = np.array([[Sxy,0,0], [0,Sxy,0], [0,0,Sz]])
    return SMatTot

# Identical dipoles, 2D, normal incidence, general vector position list
def latticeSumSMat(RvecList, k):
    
    def SMat (Rvec):
        R = np.sqrt((Rvec*Rvec).sum(axis=0))
        Rhat = Rvec/R
        I3Mat = np.identity(3)
        RRMat = np.zeros_like(I3Mat)
        for alpha in range(3):
            for beta in range(3):
                RRMat[alpha, beta] = Rhat[alpha]*Rhat[beta]
        CMat = I3Mat - RRMat
        DMat = I3Mat - 3*RRMat
        return ( np.exp(1j*k*R)/R**3 )*( (k**2)*(R**2)*CMat + (1 - 1j*k*R)*DMat )
    
    SMatTot = np.zeros_like(np.identity(3))
    length = len(RvecList)
    
    for i in range(length):
        Rvec = RvecList[i]
        SMatTot = SMatTot + SMat(Rvec)
    
    return SMatTot


# -------- Cross sections --------
# Effective dipole polarizability
# computed from the single dipole polarizability 
# and the scalar lattice sum
def alphaCDA (alpha1, S):
    return 1/(1/alpha1 - S)

# Extinction cross section
def CextCDA (S, alpha1, k): 
    p = alphaCDA(alpha1, S)
    return 4*pi*k*( p.imag )

# Absorption cross section
def CabsCDA (S, alpha1, k): 
    p = alphaCDA(alpha1, S)
    p1 = (p**2/alpha1).imag
    p2 = np.abs(p)**2
    
    return 4*pi*k*( p1 - (2/3)*(k**3)*p2 )

# Scattering cross section
def CscaCDA(S, alpha1, k):
    return CextCDA(S, alpha1, k) - CabsCDA(S, alpha1, k)


