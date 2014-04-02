# Programmed by: jasdev
#                jasdev@live.in

import flame
import laff as laff

def Set_to_diagonal_matrix_unb_var1(d, A):
    """
	Set_to_diagonal_matrix_unb_var1(vector, matrix)	
	
	Sets the diagonal elements of A to the components of vector d.

	Traverses matrix A from TOP-LEFT to BOTTOM-RIGHT,
	traverses vector d from TOP to BOTTOM 
	and sets results column-wise.
    """
    
    dT, \
    dB  = flame.part_2x1(d, \
                         0, 'TOP')

    ATL, ATR, \
    ABL, ABR  = flame.part_2x2(A, \
                               0, 0, 'TL')

    while dT.shape[0] < d.shape[0]:

        d0,     \
        delta1, \
        d2      = flame.repart_2x1_to_3x1(dT, \
                                          dB, \
                                          1, 'BOTTOM')

        A00,  a01,     A02,  \
        a10t, alpha11, a12t, \
        A20,  a21,     A22   = flame.repart_2x2_to_3x3(ATL, ATR, \
                                                       ABL, ABR, \
                                                       1, 1, 'BR')

        laff.zerov(a01)
        laff.copy(delta1, alpha11)
        laff.zerov(a21)

        dT, \
        dB  = flame.cont_with_3x1_to_2x1(d0,     \
                                         delta1, \
                                         d2,     \
                                         'TOP')

        ATL, ATR, \
        ABL, ABR  = flame.cont_with_3x3_to_2x2(A00,  a01,     A02,  \
                                               a10t, alpha11, a12t, \
                                               A20,  a21,     A22,  \
                                               'TL')

    flame.merge_2x1(dT, \
                    dB, d)

    flame.merge_2x2(ATL, ATR, \
                    ABL, ABR, A)



def Set_to_diagonal_matrix_unb_var2(d, A):
    """
	Set_to_diagonal_matrix_unb_var2(vector, matrix)	
	
	Sets the diagonal elements of A to the components of vector d.

	Traverses matrix A from TOP-LEFT to BOTTOM-RIGHT,
	traverses vector d from TOP to BOTTOM 
	and sets results row-wise.
    """
    
    dT, \
    dB  = flame.part_2x1(d, \
                         0, 'TOP')

    ATL, ATR, \
    ABL, ABR  = flame.part_2x2(A, \
                               0, 0, 'TL')

    while dT.shape[0] < d.shape[0]:

        d0,     \
        delta1, \
        d2      = flame.repart_2x1_to_3x1(dT, \
                                          dB, \
                                          1, 'BOTTOM')

        A00,  a01,     A02,  \
        a10t, alpha11, a12t, \
        A20,  a21,     A22   = flame.repart_2x2_to_3x3(ATL, ATR, \
                                                       ABL, ABR, \
                                                       1, 1, 'BR')

        laff.zerov(a10t)
        laff.copy(delta1, alpha11)
        laff.zerov(a12t)

        dT, \
        dB  = flame.cont_with_3x1_to_2x1(d0,     \
                                         delta1, \
                                         d2,     \
                                         'TOP')

        ATL, ATR, \
        ABL, ABR  = flame.cont_with_3x3_to_2x2(A00,  a01,     A02,  \
                                               a10t, alpha11, a12t, \
                                               A20,  a21,     A22,  \
                                               'TL')

    flame.merge_2x1(dT, \
                    dB, d)

    flame.merge_2x2(ATL, ATR, \
                    ABL, ABR, A)
