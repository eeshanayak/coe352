import numpy as np
from scipy.linalg import svd

def solve(num_springs, mass_list, c_list, A):
    
    # construct force matrix: force = mass * gravity
    f = np.array(mass_list) * 9.8

    # generate diagonal matrix from spring constants
    c = np.zeros((num_springs, num_springs))
    np.fill_diagonal(c, c_list)
    
    At = A.transpose()

    # cast all objects to matrices
    At = np.matrix(At)
    A = np.matrix(A)
    c = np.matrix(c)
    f = np.matrix(f)
    
    # solve for k (stiffness matrix): k = (A^t) * c * A
    k = At * c * A
    
    # invert k to sove for u
    kinv = np.linalg.inv(k)
    
    # solve for u (displacement vector): u = force * (k^-1)
    u = f * kinv
    
    # solve for e (elongation vector): e = A * u
    e = A*u.transpose()
    
    # solve for w: w = c * e
    w = c * e

    # transpose solutiosn to return as row vector
    e = e.transpose()
    w = w.transpose()
    
    return u, e, w, At, c, f