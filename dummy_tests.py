
from Set_to_zero import Set_to_zero_unb_var1, Set_to_zero_unb_var2
from Set_to_identity import Set_to_identity_unb_var1, Set_to_identity_unb_var2
from Set_to_diagonal import Set_to_diagonal_matrix_unb_var1, Set_to_diagonal_matrix_unb_var2
from Set_to_lower_triangular import Set_to_lower_triangular_matrix_unb_var1, Set_to_lower_triangular_matrix_unb_var2
from Transpose import Transpose_unb_var1, Transpose_unb_var2
from Symmetrize_from_lower_triangle import Symmetrize_from_lower_triangle_unb_var1, Symmetrize_from_lower_triangle_unb_var2
from Scale_a_matrix import Scale_a_matrix_unb_var1, Scale_a_matrix_unb_var2
from Mvmult_n import Mvmult_n_unb_var1, Mvmult_n_unb_var2
from Mvmult_t import Mvmult_t_unb_var1, Mvmult_t_unb_var2
from Tmvmult_un import Tmvmult_un_unb_var1, Tmvmult_un_unb_var2
from Tmvmult_ln import Tmvmult_ln_unb_var1, Tmvmult_ln_unb_var2
from Trmv_un import Trmv_un_unb_var1, Trmv_un_unb_var2
from Trmv_ln import Trmv_ln_unb_var1, Trmv_ln_unb_var2
from Tmvmult_lt import Tmvmult_lt_unb_var1, Tmvmult_lt_unb_var2
from Tmvmult_ut import Tmvmult_ut_unb_var1, Tmvmult_ut_unb_var2
from Trmv_lt import Trmv_lt_unb_var1, Trmv_lt_unb_var2
from Trmv_ut import Trmv_ut_unb_var1, Trmv_ut_unb_var2
from Symv_u import Symv_u_unb_var1, Symv_u_unb_var2

from GaussianElimination import GaussianElimination_unb
from ForwardSubstitution import ForwardSubstitution_unb


import numpy as np
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



###########################################
###       Tmvmult_un
###########################################
##print "Using Tmvmult_un_unb_var1"
##U = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
### Notice that U is not upper triangular.  We will only use the upper triangular part.
##print( 'U before =' )
##print( U )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Tmvmult_un_unb_var1( U, x, y )
##print( 'y after =' )
##print( y )
##print( 'y - ( np.triu( U ) * x + yold ) = ' ) #np.triu makes the matrix upper triangular
##print( y - ( np.triu( U ) * x + yold ) )
##
##print "Using Tmvmult_un_unb_var2"
##U = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
### U is not upper triangular.  We will only use the upper triangular part.
##print( 'U before =' )
##print( U )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Tmvmult_un_unb_var2( U, x, y )
##print( 'y after =' )
##print( y )
##print( 'y - ( np.triu( U ) * x + yold ) = ' ) #np.triu makes the matrix upper triangular
##print( y - ( np.triu( U ) * x + yold ) )
###########################################



###########################################
###       Tmvmult_ln
###########################################
##print "Using Tmvmult_ln_unb_var1"
##L = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
### Notice that L is not lower triangular.  We will only use the lower triangular part.
##print( 'L before =' )
##print( L )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Tmvmult_ln_unb_var1( L, x, y )
##print( 'y after =' )
##print( y )
##print( 'y - ( np.tril( L ) * x + yold ) = ' ) #np.tril makes the matrix lower triangular
##print( y - ( np.tril( L ) * x + yold ) )
##
##print "Using Tmvmult_ln_unb_var2"
##L = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
### L is not lower triangular.  We will only use the lower triangular part.
##print( 'L before =' )
##print( L )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Tmvmult_ln_unb_var2( L, x, y )
##print( 'y after =' )
##print( y )
##print( 'y - ( np.tril( L ) * x + yold ) = ' ) #np.tril makes the matrix lower triangular
##print( y - ( np.tril( L ) * x + yold ) )
###########################################



###########################################
###       Trmv_un
###########################################
##print "Using Trmv_un_unb_var1"
##U = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##xold = matrix( random.rand( 4,1 ) )
### Notice that U is not upper triangular.  We will only use the upper triangular part.
##print( 'U before =' )
##print( U )
##print( 'x before =' )
##print( x )
##laff.copy( x, xold )   # save the original vector x
##Trmv_un_unb_var1( U, x )
##print( 'x after =' )
##print( x )
##print( np.triu( U ) * xold )
##print( 'x - ( np.triu( U ) * xold ) = ' ) #np.triu makes the matrix upper triangular
##print( x - ( np.triu( U ) * xold ) )
##
##print "Using Trmv_un_unb_var2"
##U = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##xold = matrix( random.rand( 4,1 ) )
### U is not upper triangular.  We will only use the upper triangular part.
##print( 'U before =' )
##print( U )
##print( 'x before =' )
##print( x )
##laff.copy( x, xold )   # save the original vector y
##Trmv_un_unb_var2( U, x )
##print( 'x after =' )
##print( x )
##print( 'x - ( np.triu( U ) * xold ) = ' ) #np.triu makes the matrix upper triangular
##print( x - ( np.triu( U ) * xold ) )
###########################################



###########################################
###       Trmv_ln
###########################################
##print "Using Trmv_ln_unb_var1"
##L = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##xold = matrix( random.rand( 4,1 ) )
### Notice that L is not lower triangular.  We will only use the lower triangular part.
##print( 'L before =' )
##print( L )
##print( 'x before =' )
##print( x )
##laff.copy( x, xold )   # save the original vector x
##Trmv_ln_unb_var1( L, x )
##print( 'x after =' )
##print( x )
##print( np.tril( L ) * xold )
##print( 'x - ( np.tril( L ) * xold ) = ' ) #np.tril makes a matrix lower triangular
##print( x - ( np.tril( L ) * xold ) )
##
##print "Using Trmv_ln_unb_var2"
##L = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##xold = matrix( random.rand( 4,1 ) )
### L is not lower triangular.  We will only use the lower triangular part.
##print( 'L before =' )
##print( L )
##print( 'x before =' )
##print( x )
##laff.copy( x, xold )   # save the original vector y
##Trmv_ln_unb_var2( L, x )
##print( 'x after =' )
##print( x )
##print( 'x - ( np.tril( L ) * xold ) = ' ) #np.tril makes the matrix lower triangular
##print( x - ( np.tril( L ) * xold ) )
###########################################




###########################################
###       Tmvmult_lt
###########################################
##print "Using Tmvmult_lt_unb_var1"
##L = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
### Notice that L is not lower triangular.  We will only use the lower triangular part.
##print( 'L before =' )
##print( L )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Tmvmult_lt_unb_var1( L, x, y )
##print( 'y after =' )
##print( y )
###np.tril makes the matrix lower triangular
##print( 'y - ( np.transpose( np.tril( L ) ) * x + yold ) = ' )
##print( y - ( np.transpose( np.tril( L ) ) * x + yold ) )
##
##
##print "Using Tmvmult_lt_unb_var2"
##L = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
### L is not lower triangular.  We will only use the lower triangular part.
##print( 'L before =' )
##print( L )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Tmvmult_lt_unb_var2( L, x, y )
##print( 'y after =' )
##print( y )
###np.tril makes the matrix lower triangular
##print( 'y - ( np.transpose( np.tril( L ) ) * x + yold ) = ' )
##print( y - ( np.transpose( np.tril( L ) ) * x + yold ) )
###########################################




###########################################
###       Tmvmult_ut
###########################################
##print "Using Tmvmult_ut_unb_var1"
##U = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
### Notice that U is not upper triangular.  We will only use the upper triangular part.
##print( 'U before =' )
##print( U )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Tmvmult_ut_unb_var1( U, x, y )
##print( 'y after =' )
##print( y )
###np.triu makes the matrix upper triangular
##print( 'y - ( np.transpose( np.triu( U ) ) * x + yold ) = ' )
##print( y - ( np.transpose( np.triu( U ) ) * x + yold ) )
##
##
##print "Using Tmvmult_ut_unb_var2"
##U = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
### U is not upper triangular.  We will only use the upper triangular part.
##print( 'U before =' )
##print( U )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##laff.copy( y, yold )   # save the original vector y
##Tmvmult_ut_unb_var2( U, x, y )
##print( 'y after =' )
##print( y )
###np.triu makes the matrix upper triangular
##print( 'y - ( np.transpose( np.triu( U ) ) * x + yold ) = ' )
##print( y - ( np.transpose( np.triu( U ) ) * x + yold ) )
###########################################




###########################################
###       Trmv_lt
###########################################
##print "Using Trmv_lt_unb_var1"
##L = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##xold = matrix( random.rand( 4,1 ) )
### Notice that L is not lower triangular.  We will only use the lower triangular part.
##print( 'L before =' )
##print( L )
##print( 'x before =' )
##print( x )
##laff.copy( x, xold )   # save the original vector x
##Trmv_lt_unb_var1( L, x )
##print( 'x after =' )
##print( x )
###np.tril makes the matrix lower triangular
##print( 'x - ( np.transpose( np.tril( L ) ) * xold ) = ' )
##print( x - ( np.transpose( np.tril( L ) ) * xold ) )
##
##print "Using Trmv_lt_unb_var2"
##L = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##xold = matrix( random.rand( 4,1 ) )
### L is not lower triangular.  We will only use the lower triangular part.
##print( 'L before =' )
##print( L )
##print( 'x before =' )
##print( x )
##laff.copy( x, xold )   # save the original vector y
##Trmv_lt_unb_var2( L, x )
##print( 'x after =' )
##print( x )
###np.tril makes the matrix lower triangular
##print( 'x - ( np.transpose( np.tril( L ) ) * xold ) = ' )
##print( x - ( np.transpose( np.tril( L ) ) * xold ) )
###########################################



###########################################
###       Trmv_ut
###########################################
##print "Using Trmv_ut_unb_var1"
##U = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##xold = matrix( random.rand( 4,1 ) )
### Notice that U is not upper triangular.  We will only use the upper triangular part.
##print( 'U before =' )
##print( U )
##print( 'x before =' )
##print( x )
##laff.copy( x, xold )   # save the original vector x
##Trmv_ut_unb_var1( U, x )
##print( 'x after =' )
##print( x )
###np.triu makes the matrix upper triangular
##print( 'x - ( np.transpose( np.triu( U ) ) * xold ) = ' )
##print( x - ( np.transpose( np.triu( U ) ) * xold ) )
##
##print "Using Trmv_ut_unb_var2"
##U = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##xold = matrix( random.rand( 4,1 ) )
### U is not upper triangular.  We will only use the upper triangular part.
##print( 'U before =' )
##print( U )
##print( 'x before =' )
##print( x )
##laff.copy( x, xold )   # save the original vector y
##Trmv_ut_unb_var2( U, x )
##print( 'x after =' )
##print( x )
###np.triu makes the matrix upper triangular
##print( 'x - ( np.transpose( np.triu( U ) ) * xold ) = ' )
##print( x - ( np.transpose( np.triu( U ) ) * xold ) )
###########################################




###########################################
###       Symv_u
###########################################
##print "Using Symv_u_unb_var1"
##A = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
##print( 'A before =' )
##print( A )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##Asymm = np.triu( A ) + np.transpose( np.triu( A, 1 ) )
##laff.copy( y, yold )   # save the original vector y
##Symv_u_unb_var1( A, x, y )
##print( 'y after =' )
##print( y )
##print( 'y - ( Asymm * x + yold ) = ' )
##print( y - ( Asymm * x + yold ) )
##
##
##print "Using Symv_u_unb_var2"
##A = matrix( random.rand( 4,4 ) )
##x = matrix( random.rand( 4,1 ) )
##y = matrix( random.rand( 4,1 ) )
##yold = matrix( random.rand( 4,1 ) )
##print( 'A before =' )
##print( A )
##print( 'x before =' )
##print( x )
##print( 'y before =' )
##print( y )
##Asymm = np.triu( A ) + np.transpose( np.triu( A, 1 ) )
##laff.copy( y, yold )   # save the original vector y
##Symv_u_unb_var2( A, x, y )
##print( 'y after =' )
##print( y )
##print( 'y - ( Asymm * x + yold ) = ' )
##print( y - ( Asymm * x + yold ) )
###########################################




###########################################
###       GaussianElimination
###               &
###       ForwardSubstitution
###########################################
##print "Using GaussianElimination_unb"
##L = np.matrix( ' 1, 0, 0. 0;\
##                -2, 1, 0, 0;\
##                 1,-3, 1, 0;\
##                 2, 3,-1, 1' )
##U = np.matrix( ' 2,-1, 3,-2;\
##                 0,-2, 1,-1;\
##                 0, 0, 1, 2;\
##                 0, 0, 0, 3' )
##A = L * U
##print( 'A = ' )
##print( A )
### create a solution vector x
##x = np.matrix( '-1;\
##                 2;\
##                 1;\
##                -2' )
### store the original value of x
##xold = np.matrix( np.copy( x ) )
### create a solution vector b so that A x = b
##b = A * x
##print( 'b = ' )
##print( b )
##L0 = np.matrix( ' 1, 0, 0, 0;\
##                  2, 1, 0, 0;\
##                 -1, 0, 1, 0;\
##                 -2, 0, 0, 1' );
##A = L0 * A
##print( A )
##L1 = np.matrix( ' 1, 0, 0, 0;\
##                  0, 1, 0, 0;\
##                  0, 3, 1, 0;\
##                  0, -3, 0, 1' );
##A = L1 * A
##print( A )
##L2 = np.matrix( ' 1, 0, 0, 0;\
##                  0, 1, 0, 0;\
##                  0, 0, 1, 0;\
##                  0, 0, 1, 1' );
##A = L2 * A
##print( A )
##b = L0 * b
##b = L1 * b
##b = L2 * b
##print( 'b after forward substitution (application of Gauss transforms):' )
##print( b )
##
##x[ 3 ] = b[ 3 ] / A[ 3,3 ]
##x[ 2 ] = ( b[ 2 ] - A[ 2,3 ] * x[ 3 ] ) / A[ 2,2 ]
##x[ 1 ] = ( b[ 1 ] - A[ 1,2 ] * x[ 2 ] - A[ 1,3 ] * x[ 3 ] ) / A[ 1,1 ]
##x[ 0 ] = ( b[ 0 ] - A[ 0,1 ] * x[ 1 ] - A[ 0,2 ] * x[ 2 ]- A[ 0,3 ] * x[ 3 ] ) / A[ 0,0 ]
##
##print( 'x = ' )
##print( x )
##print( 'x - xold' )
##print( x - xold )
##
### recreate matrix A
##A = L * U
##
### recreate the right-hand side
##b = A * xold
##
### apply Gaussian elimination to matrix A
##GaussianElimination_unb( A )
##
##print( A )
##print( 'Original L' )
##print( L )
##print( 'Original U' )
##print( U )
##
##
##
##print( A )
##print( b )
##ForwardSubstitution_unb( A, b )
##print( 'updated b' )
##print( b )
##x[ 3 ] = b[ 3 ] / A[ 3,3 ]
##x[ 2 ] = ( b[ 2 ] - A[ 2,3 ] * x[ 3 ] ) / A[ 2,2 ]
##x[ 1 ] = ( b[ 1 ] - A[ 1,2 ] * x[ 2 ] - A[ 1,3 ] * x[ 3 ] ) / A[ 1,1 ]
##x[ 0 ] = ( b[ 0 ] - A[ 0,1 ] * x[ 1 ] - A[ 0,2 ] * x[ 2 ]- A[ 0,3 ] * x[ 3 ] ) / A[ 0,0 ]
##print( 'x = ' )
##print( x )
##print( 'x - xold' )
##print( x - xold )
##
###########################################
