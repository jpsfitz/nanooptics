# ======== Header for ipyparallel kernels  ========
import os, sys, types
import ipyparallel as ipp


# -------- Parallel kernels --------
print("Initializing cluster ...")

# variables
global kernels, cluster, nKernels
kernels = ipp.Client()
print("   Client variable \'kernels\'")
cluster = kernels[:]
print("   Cluster Direct View variable \'cluster\'")
nKernels = len(kernels.ids)
print("   Variable \'nKernels\' =",nKernels)

# initialize parallel kernels
with cluster.sync_imports():
    import mie
    import mie_local
