import laff
import numpy as np

#########################################
# copy tests
print "Testing copy()"

x = np.matrix( '1 2 3' )
y = np.matrix('0 -2 -3')
print( "x = " )
print( x )
print( "y = " )
print( y )
laff.copy( x, y )
print( "y = " )
print( y )
assert np.array_equal(x,y), "error!"

#########################################



