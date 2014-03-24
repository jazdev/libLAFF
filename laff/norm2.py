import laff
import numpy as np
from math import sqrt

def norm2( x ):
    """



    """
    assert type(x) is np.matrix and len(x.shape) is 2, "laff.norm2: vector x must be a 2D numpy.matrix"
	
    m, n = np.shape(x)
	
    assert m is 1 or n is 1, "laff.norm2: x is not a vector"

    y = np.matrix( np.zeros( (m,n) ) )
    laff.copy( x, y )
	
    alpha = 0
    maxval = y[ 0, 0 ]

    if m is 1: #y is a row
	for i in range(n):
	    if abs(y[ 0, i ]) > maxval:
		maxval = abs(y[ 0, i ])
		
    elif n is 1: #y is a column
	for i in range(m):
	    if abs(y[ i, 0 ]) > maxval:
		maxval = abs(y[ i, 0 ])

    if abs(maxval) < 1e-7:
	return 0

    laff.scal( 1.0/maxval, y )
	
    alpha = maxval * sqrt( laff.dot( y, y ) )
	
    return alpha
