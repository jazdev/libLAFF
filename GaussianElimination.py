# Programmed by: Jasdev SIngh
#                

import flame
import laff as laff

def GaussianElimination_unb(A):
    """
	GaussianElimination_unb(matrix)	

	Computes the Gauss Transform of the input matrix.

	Traverses matrix A from TOP-LEFT to BOTTOM-RIGHT.
    """
    ATL, ATR, \
    ABL, ABR  = flame.part_2x2(A, \
                               0, 0, 'TL')

    while ATL.shape[0] < A.shape[0]:

        A00,  a01,     A02,  \
        a10t, alpha11, a12t, \
        A20,  a21,     A22   = flame.repart_2x2_to_3x3(ATL, ATR, \
                                                       ABL, ABR, \
                                                       1, 1, 'BR')

        laff.invscal( alpha11, a21 )        #  a21 := a21 / alpha11
        laff.ger( -1.0, a21, a12t, A22 )    #  A22 := A22 - a21 * a12t

        ATL, ATR, \
        ABL, ABR  = flame.cont_with_3x3_to_2x2(A00,  a01,     A02,  \
                                               a10t, alpha11, a12t, \
                                               A20,  a21,     A22,  \
                                               'TL')

    flame.merge_2x2(ATL, ATR, \
                    ABL, ABR, A)
