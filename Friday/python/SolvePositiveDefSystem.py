import numpy as np
import sys
import numpy.linalg as nl
from CG import *
from cholesky import *
from Matrices import *

# Set everything up
N = 10
main = 2.0*np.ones(N)
offset = -1.0*np.ones(N-1)
A = MakeTridiag(main, offset)
b = np.random.random((N, 1))

# Solve using conjugate gradient
x_i = np.ones((N, 1))
r_i = b - np.dot(A, x_i)
d_i = r_i
for it in range(N):
    x_i, r_i, d_i = CG_Iteration(x_i, r_i, d_i,  A)

# Solve using Cholesky factors.
L = cholesky(A)
z = nl.solve(L, b)
x = nl.solve(np.transpose(L), z)

print(np.max(np.abs(x - x_i)))