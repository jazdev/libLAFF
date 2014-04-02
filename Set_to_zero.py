# Programmed by: jasdev

import flame
import laff as laff

def Set_to_zero_unb_var1(A):
    """
	Set_to_zero_unb_var1(matrix)	
	
	Sets the input matrix to zeros.
	Traverses input matrix from LEFT to RIGHT
	and sets results column-wise.
    """

    AL, \
    AR = flame.part_1x2(A, \
                        0, 'LEFT')

    while AL.shape[1] < A.shape[1]:

        A0, \
        a1, \
        A2 = flame.repart_1x2_to_1x3(AL, \
                                     AR, \
                                     1, 'RIGHT')

        laff.zerov(a1)

        AL, \
        AR = flame.cont_with_1x3_to_1x2(A0, \
                                        a1, \
                                        A2, 'LEFT')

    flame.merge_1x2(AL, \
                    AR, A)


def Set_to_zero_unb_var2(A):
    """
	Set_to_zero_unb_var2(matrix)	
	
	Sets the input matrix to zeros.
	Traverses input matrix from TOP to BOTTOM
	and sets results column-wise.
    """

    AT, \
    AB  = flame.part_2x1(A, \
                         0, 'TOP')

    while AT.shape[0] < A.shape[0]:

        A0,  \
        a1t, \
        A2   = flame.repart_2x1_to_3x1(AT, \
                                       AB, \
                                       1, 'BOTTOM')

        laff.zerov(a1t)

        AT, \
        AB  = flame.cont_with_3x1_to_2x1(A0,  \
                                         a1t, \
                                         A2,  \
                                         'TOP')

    flame.merge_2x1(AT, \
                    AB, A)
