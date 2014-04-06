# Programmed by: Jasdev Singh
#                

import flame
import laff as laff

def Symmetrize_from_lower_triangle_unb_var1(A):
    """
	Symmetrize_from_lower_triangle_unb_var1(matrix)	
	
	Makes square matrix A symmetric by copying the
	lower triangular part in its upper triangular part.

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

        laff.copy(a01,a10t)

        ATL, ATR, \
        ABL, ABR  = flame.cont_with_3x3_to_2x2(A00,  a01,     A02,  \
                                               a10t, alpha11, a12t, \
                                               A20,  a21,     A22,  \
                                               'TL')

    flame.merge_2x2(ATL, ATR, \
                    ABL, ABR, A)


def Symmetrize_from_lower_triangle_unb_var2(A):
    """
	Symmetrize_from_lower_triangle_unb_var2(matrix)	
	
	Makes square matrix A symmetric by copying the
	lower triangular part in its upper triangular part.

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

        laff.copy(a12t,a21)

        ATL, ATR, \
        ABL, ABR  = flame.cont_with_3x3_to_2x2(A00,  a01,     A02,  \
                                               a10t, alpha11, a12t, \
                                               A20,  a21,     A22,  \
                                               'TL')

    flame.merge_2x2(ATL, ATR, \
                    ABL, ABR, A)
