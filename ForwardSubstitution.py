# Programmed by: Jasdev SIngh
#                

import flame
import laff

def ForwardSubstitution_unb(A, b):
    """
	ForwardSubstitution_unb(matrix, vector)	

	Computes coefficients using Forward Substituion.

	Traverses matrix A from TOP-LEFT to BOTTOM-RIGHT,
	vector b from TOP to BOTTOM.
    """
    ATL, ATR, \
    ABL, ABR  = flame.part_2x2(A, \
                               0, 0, 'TL')

    bT, \
    bB  = flame.part_2x1(b, \
                         0, 'TOP')

    while ATL.shape[0] < A.shape[0]:

        A00,  a01,     A02,  \
        a10t, alpha11, a12t, \
        A20,  a21,     A22   = flame.repart_2x2_to_3x3(ATL, ATR, \
                                                       ABL, ABR, \
                                                       1, 1, 'BR')

        b0,    \
        beta1, \
        b2     = flame.repart_2x1_to_3x1(bT, \
                                         bB, \
                                         1, 'BOTTOM')


        laff.axpy( -beta1, a21, b2 )


        ATL, ATR, \
        ABL, ABR  = flame.cont_with_3x3_to_2x2(A00,  a01,     A02,  \
                                               a10t, alpha11, a12t, \
                                               A20,  a21,     A22,  \
                                               'TL')

        bT, \
        bB  = flame.cont_with_3x1_to_2x1(b0,    \
                                         beta1, \
                                         b2,    \
                                         'TOP')

    flame.merge_2x1(bT, \
                    bB, b)
