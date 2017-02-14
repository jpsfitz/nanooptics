# ======== Lattice computation codes ======
# Generates a lattice for CDA computations
# Generates simplified lattice lists for simplified 2D CDA codes


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
    print("  ... lattice generation functions loaded:")
    print("       hexagonal 2D")
    return



# -------- Hexagonal lattice --------
# Basis vectors
a1Hex = np.array([1, 0, 0])
a2Hex = np.array([0.5, abs(np.sqrt(3)/2), 0])
a3Hex = np.array([0, 0, 1])

# Lists of position vectors and magnitudes
# in units of lattice spacing
# excludes the (0,0,0)
def RvecRmagListsHex (maxR):
    # Basis vectors
    a1 = np.array([1, 0, 0])
    a2 = np.array([0.5, abs(np.sqrt(3)/2), 0])
    
    # Limits 
    a1dota2 = (a1*a2).sum(axis=0)
    alphaMax = int(ceil( maxR*(1 + 0.5*a1dota2) ))
    alphaMin = -alphaMax
    def betaMax (alpha): 
        return int(round(-alpha*a1dota2 + np.sqrt( alphaMax**2 - alpha**2 + (alpha*a1dota2)**2 )))
    def betaMin (alpha): 
        return int(ceil(-alpha*a1dota2 - np.sqrt( alphaMax**2 - alpha**2 + (alpha*a1dota2)**2 )))
    
    # initial list of position vectors and magnitudes
    RvecList = []
    RmagList = []
    for alpha in range(alphaMin, alphaMax + 1):
        for beta in range(betaMin(alpha), betaMax(alpha)):
            Rvec = alpha*a1 + beta*a2
            Rmag = np.sqrt((Rvec*Rvec).sum())
            RvecList.append(Rvec)
            RmagList.append(Rmag)
    
    # exclude origin and sites too far away 
    RmagArray = np.asarray(RmagList)
    RvecArray = np.asarray(RvecList)
    select = ((RmagArray <= maxR) & (RmagArray > 0))
    RmagList = list(RmagArray[select])
    RvecList = list(RvecArray[select])
    
    return RvecList, RmagList

# Lists of unique magnitudes and number of sites with that magnitude
# in units of lattice spacing
def RmagNListHex (maxR):
    accuracy = 12
    rnd = 10**accuracy
    RvecList0, RmagList0 = RvecRmagListsHex(maxR)
    RmagArray = (1/rnd)*np.round(rnd*np.asarray(RmagList0))
    RmagArray, NArray = np.unique(RmagArray, return_counts=True)
    RmagList, NList = list(RmagArray), list(NArray)
    return RmagList, NList

