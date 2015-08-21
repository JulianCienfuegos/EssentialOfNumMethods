import numpy as np

def cholesky(M):
    N = M.shape[0]
    L = np.zeros((N,N))
    for i in range(N):
        L[i, i] = np.sqrt(M[i, i])
        M[i,i] =  L[i,i]
        L[i+1:, i] = M[i+1:, i] / L[i,i] #Various ways to deal with this. This is out of bounds after all.
        M[i+1:, i] = L[i+1:, i] 
        M[i+1:, i+1:] -=  np.outer(M[i+1:, i], M[i+1:, i] ) # can't use dot(). Dot gives an inner product, use outer!!!
    return L