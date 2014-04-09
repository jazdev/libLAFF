# Programmed by: Jasdev Singh
#                

import flame
import laff as laff

def Scale_a_matrix_unb_var1(beta, A):
    """
	Scale_a_matrix_unb_var1(scalar, matrix)	
	
	Scales matrix A by a factor of beta.

	Traverses matrix A from LEFT to RIGHT.
    """
    AL, AR = flame.part_1x2(A, \
                            0, 'LEFT')

    while AL.shape[1] < A.shape[1]:

        A0, a1, A2 = flame.repart_1x2_to_1x3(AL, AR, \
                                             1, 'RIGHT')

        laff.scal(beta,a1)

        AL, AR = flame.cont_with_1x3_to_1x2(A0, a1, A2, \
                                            'LEFT')

    flame.merge_1x2(AL, AR, A)


def Scale_a_matrix_unb_var2(beta, A):
    """
	Scale_a_matrix_unb_var2(scalar, matrix)	
	
	Scales matrix A by a factor of beta.

	Traverses matrix A from TOP to BOTTOM.
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

        laff.scal(beta,a1t)

        AT, \
        AB  = flame.cont_with_3x1_to_2x1(A0,  \
                                         a1t, \
                                         A2,  \
                                         'TOP')

    flame.merge_2x1(AT, \
                    AB, A)
