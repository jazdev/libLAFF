
from Set_to_zero import Set_to_zero_unb_var1, Set_to_zero_unb_var2
from Set_to_identity import Set_to_identity_unb_var1, Set_to_identity_unb_var2
from Set_to_diagonal import Set_to_diagonal_matrix_unb_var1, Set_to_diagonal_matrix_unb_var2
from Set_to_lower_triangular import Set_to_lower_triangular_matrix_unb_var1, Set_to_lower_triangular_matrix_unb_var2
from Transpose import Transpose_unb_var1, Transpose_unb_var2
from Symmetrize_from_lower_triangle import Symmetrize_from_lower_triangle_unb_var1, Symmetrize_from_lower_triangle_unb_var2
from Scale_a_matrix import Scale_a_matrix_unb_var1, Scale_a_matrix_unb_var2
from Mvmult_n import Mvmult_n_unb_var1, Mvmult_n_unb_var2
from Mvmult_t import Mvmult_t_unb_var1, Mvmult_t_unb_var2


from numpy import random
from numpy import matrix
import laff as laff

###########################################
###       Set_to_zero
###########################################
##print "Using Set_to_zero_unb_var1"
##A = matrix( random.rand( 5,4 ) )
##print( 'A before =' )
##print( A )
##Set_to_zero_unb_var1( A )
##print( 'A after =' )
##print( A )
##
##print "Using Set_to_zero_unb_var2"
##A = matrix( random.rand( 5,4 ) )
##print( 'A before =' )
##print( A )
##Set_to_zero_unb_var2( A )
##print( 'A after =' )
##print( A )
###########################################


###########################################
###       Set_to_identity
###########################################
##print "Using Set_to_identity_unb_var1"
##A = matrix( random.rand( 5,5 ) )
##print( 'A before =' )
##print( A )
##Set_to_identity_unb_var1( A )
##print( 'A after =' )
##print( A )
##
##print "Using Set_to_identity_unb_var2"
##A = matrix( random.rand( 5,5 ) )
##print( 'A before =' )
##print( A )
##Set_to_identity_unb_var2( A )
##print( 'A after =' )
##print( A )
###########################################


###########################################
###       Set_to_diagonal
###########################################
##print "Using Set_to_diagonal_matrix_unb_var1"
##A = matrix( random.rand( 5,5 ) )
##d = matrix( random.rand( 5,1 ) )
##print( 'A before =' )
##print( A )
##print( 'd before =' )
##print( d )
##Set_to_diagonal_matrix_unb_var1( d, A )
##print( 'A after =' )
##print( A )
##
##print "Using Set_to_diagonal_matrix_unb_var2"
##A = matrix( random.rand( 5,5 ) )
##d = matrix( random.rand( 5,1 ) )
##print( 'A before =' )
##print( A )
##print( 'd before =' )
##print( d )
##Set_to_diagonal_matrix_unb_var2( d, A )
##print( 'A after =' )
##print( A )
###########################################


###########################################
###       Set_to_lower_triangular
###########################################
##print "Using Set_to_lower_triangular_matrix_unb_var1"
##A = matrix( random.rand( 5,5 ) )
##print( 'A before =' )
##print( A )
##Set_to_lower_triangular_matrix_unb_var1( A )
##print( 'A after =' )
##print( A )
##
##print "Using Set_to_lower_triangular_matrix_unb_var2"
##A = matrix( random.rand( 5,5 ) )
##print( 'A before =' )
##print( A )
##Set_to_lower_triangular_matrix_unb_var2( A )
##print( 'A after =' )
##print( A )
###########################################



###########################################
###       Transpose
###########################################
##print "Using Transpose_unb_var1"
##A = matrix( random.rand( 5,4 ) )
##B = matrix( random.rand( 4,5 ) )
##print( 'A ' )
##print( A )
##print( 'B before =' )
##print( B )
##Transpose_unb_var1( A, B )
##print( 'A ' )
##print( A )
##print( 'B after =' )
##print( B )
##
##print "Using Transpose_unb_var1"
##A = matrix( random.rand( 5,4 ) )
##B = matrix( random.rand( 4,5 ) )
##print( 'A ' )
##print( A )
##print( 'B before =' )
##print( B )
##Transpose_unb_var2( A, B )
##print( 'A ' )
##print( A )
##print( 'B after =' )
##print( B )
###########################################


###########################################
###       Symmetrize_from_lower_triangle
###########################################
##print "Using Symmetrize_from_lower_triangle_unb_var1"
##A = matrix( random.rand( 5,5 ) )
##print( 'A before =' )
##print( A )
##Symmetrize_from_lower_triangle_unb_var1( A )
##print( 'A after =' )
##print( A )
##
##print "Using Symmetrize_from_lower_triangle_unb_var2"
##A = matrix( random.rand( 5,5 ) )
##print( 'A before =' )
##print( A )
##Symmetrize_from_lower_triangle_unb_var2( A )
##print( 'A after =' )
##print( A )
###########################################


###########################################
###       Scale_a_matrix
###########################################
##print "Using Scale_a_matrix_unb_var1"
##beta = matrix( '2.' )
##A = matrix( random.rand( 5,4 ) )
##print( 'beta = ' )
##print( beta )
##print( 'A before =' )
##print( A )
##Scale_a_matrix_unb_var1( beta, A )
##print( 'A after =' )
##print( A )
##
##print "Using Scale_a_matrix_unb_var2"
##beta = matrix( '2' );
##A = matrix( random.rand( 5,4 ) )
##print( 'A before =' )
##print( A )
##Scale_a_matrix_unb_var2( beta, A )
##print( 'A after =' )
##print( A )
###########################################


###########################################
###       Mvmult_n
###########################################
##print "Using Mvmult_n_unb_var1"
##A = matrix( random.rand( 4,3 ) )
##x = matrix( random.rand( 3,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
##print( 'A before =' )
##print( A )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Mvmult_n_unb_var1( A, x, y )
##print( 'y after =' )
##print( y )
##print( 'y - ( A * x + yold ) = ' )
##print( y - ( A * x + yold ) )
##
##print "Using Mvmult_n_unb_var2"
##A = matrix( random.rand( 4,3 ) )
##x = matrix( random.rand( 3,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
##print( 'y before =' )
##print( y )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Mvmult_n_unb_var2( A, x, y )
##print( 'y after =' )
##print( y )
##print( 'y - ( A * x + yold ) = ' )
##print( y - ( A * x + yold ) )
###########################################



###########################################
###       Mvmult_t
###########################################
##print "Using Mvmult_t_unb_var1"
##A = matrix( random.rand( 3,4 ) )
##x = matrix( random.rand( 3,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
##print( 'A before =' )
##print( A )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Mvmult_t_unb_var1( A, x, y )
##print( 'y after =' )
##print( y )
##print( 'y - ( transpose( A ) * x + yold ) = ' )
##print( y - ( transpose( A ) * x + yold ) )
##
##print "Using Mvmult_t_unb_var2"
##A = matrix( random.rand( 3,4 ) )
##x = matrix( random.rand( 3,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
##print( 'A before =' )
##print( y )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Mvmult_t_unb_var2( A, x, y )
##print( 'y after =' )
##print( y )
##print( 'y - ( transpose( A ) * x + yold ) = ' )
##print( y - ( transpose( A ) * x + yold ) )
###########################################




