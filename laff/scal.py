# This routine is used for scaling vector X by a factor of alpha
# X may be a row or column vector

from numpy import *

def scal(alpha, x):
    """
    Compute alpha * x, overwriting x
    
    x can be row or column vectors.
    """
    m_x, n_x = x.shape

    if m_x is 1: # x is a row
        for i in range(n_x): x[0, i] = alpha * x[0, i]
            
    elif n_x is 1: # x is a column
        for i in range(m_x): x[i, 0] = alpha * x[i, 0]
