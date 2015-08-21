import numpy as np

def CG_Iteration(x_i, r_i, d_i, A):
    """This function will perform one iteration of the conjugate gradient
    algorithm as described in An Introduction to the Conjugate Gradient
    Method Without the Agonizing Pain. All of the inputs are numpy arrays.
    We don't store A as a matrix, but as a 2D array. For reasons why, see the 
    numpy documentation online where they compare the pros and cons of arrays
    and matrices."""
    num = np.dot(np.transpose(r_i), r_i)
    denom = np.dot(np.transpose(d_i), np.dot(A, d_i))
    alpha = num/denom
    x_ip1 = x_i + alpha*d_i
    r_ip1 = r_i - alpha*np.dot(A, d_i)
    beta = (np.dot(np.transpose(r_ip1), r_ip1))/(np.dot(np.transpose(r_i), r_i))
    d_ip1 = r_ip1 + beta*d_i
    return x_ip1, r_ip1, d_ip1

