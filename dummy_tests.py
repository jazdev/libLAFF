
from Set_to_zero import Set_to_zero_unb_var1
from Set_to_identity import Set_to_identity_unb_var1

from numpy import random
from numpy import matrix

###########################################
###       Set_to_zero
###########################################
##A = matrix( random.rand( 5,4 ) )
##
##print( 'A before =' )
##print( A )
##
##Set_to_zero_unb_var1( A )
##
##print( 'A after =' )
##print( A )
###########################################


#########################################
#       Set_to_identity
#########################################
A = matrix( random.rand( 5,5 ) )

print( 'A before =' )
print( A )

Set_to_identity_unb_var1( A )

print( 'A after =' )
print( A )
#########################################

