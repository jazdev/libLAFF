# Programmed by: jasdev
#                

import flame
import laff as laff

def Set_to_identity_unb_var1(A):
    """
	Set_to_identity_unb_var1(matrix)	
	
	Sets the input matrix to the Identity matrix.
	Traverses input matrix from TOP-LEFT to BOTTOM-RIGHT
	and sets results column-wise.
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

        laff.zerov(a01)
        laff.onev(alpha11)
        laff.zerov(a21)

        ATL, ATR, \
        ABL, ABR  = flame.cont_with_3x3_to_2x2(A00,  a01,     A02,  \
                                               a10t, alpha11, a12t, \
                                               A20,  a21,     A22,  \
                                               'TL')

    flame.merge_2x2(ATL, ATR, \
                    ABL, ABR, A)


def Set_to_identity_unb_var2(A):
    """
	Set_to_identity_unb_var2(matrix)	
	
	Sets the input matrix to the Identity matrix.
	Traverses input matrix from TOP-LEFT to BOTTOM-RIGHT
	and dets results row-wise.
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

        laff.zerov(a10t)
        laff.onev(alpha11)
        laff.zerov(a12t)

        ATL, ATR, \
        ABL, ABR  = flame.cont_with_3x3_to_2x2(A00,  a01,     A02,  \
                                               a10t, alpha11, a12t, \
                                               A20,  a21,     A22,  \
                                               'TL')

    flame.merge_2x2(ATL, ATR, \
                    ABL, ABR, A)
