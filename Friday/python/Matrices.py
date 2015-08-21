import numpy as np

def MakeTridiag(main, offset_one):
    """This function will make a tridiagonal 2D array (NOT a matrix)
    which has the main array on its main diagonal and the offset_one 
    array on its super and sub diagonals.
    """
    return np.diag(main) + np.diag(offset_one, k = -1) + np.diag(offset_one, k = 1)