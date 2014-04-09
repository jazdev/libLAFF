# Programmed by: Jasdev Singh
#                

import flame
import laff as laff

def Mvmult_n_unb_var1(A, x, y):
    """
	Mvmult_n_unb_var1(matrix, vector, vector)	

	Compuyes y = A * x + y

	Traverses matrix A from TOP to BOTTOM,
	vector y from TOP to BOTTOM.
    """
    AT, \
    AB  = flame.part_2x1(A, \
                         0, 'TOP')

    yT, \
    yB  = flame.part_2x1(y, \
                         0, 'TOP')

    while AT.shape[0] < A.shape[0]:

        A0,  \
        a1t, \
        A2   = flame.repart_2x1_to_3x1(AT, \
                                       AB, \
                                       1, 'BOTTOM')

        y0,   \
        psi1, \
        y2    = flame.repart_2x1_to_3x1(yT, \
                                        yB, \
                                        1, 'BOTTOM')

        laff.dots( a1t, x, psi1 )

        AT, \
        AB  = flame.cont_with_3x1_to_2x1(A0,  \
                                         a1t, \
                                         A2,  \
                                         'TOP')

        yT, \
        yB  = flame.cont_with_3x1_to_2x1(y0,   \
                                         psi1, \
                                         y2,   \
                                         'TOP')

    flame.merge_2x1(yT, \
                    yB, y)

