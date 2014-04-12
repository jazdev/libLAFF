# Programmed by: Jasdev Singh
#                

import flame
import laff as laff

def Mvmult_t_unb_var1(A, x, y):
    """
	Mvmult_t_unb_var1(matrix, vector, vector)	

	Compuyes y = A' * x + y using DOT products.

	Traverses matrix A from LEFT to RIGHT,
	vector y from TOP to BOTTOM.
    """
    AL, AR = flame.part_1x2(A, \
                            0, 'LEFT')

    yT, \
    yB  = flame.part_2x1(y, \
                         0, 'TOP')

    while AL.shape[1] < A.shape[1]:

        A0, a1, A2 = flame.repart_1x2_to_1x3(AL, AR, \
                                             1, 'RIGHT')

        y0,   \
        psi1, \
        y2    = flame.repart_2x1_to_3x1(yT, \
                                        yB, \
                                        1, 'BOTTOM')

        laff.dots( a1, x, psi1 )

        AL, AR = flame.cont_with_1x3_to_1x2(A0, a1, A2, \
                                            'LEFT')

        yT, \
        yB  = flame.cont_with_3x1_to_2x1(y0,   \
                                         psi1, \
                                         y2,   \
                                         'TOP')

    flame.merge_2x1(yT, \
                    yB, y)



def Mvmult_t_unb_var2(A, x, y):
    """
	Mvmult_t_unb_var2(matrix, vector, vector)	

	Compuyes y = A' * x + y using AXPY operations.

	Traverses matrix A from TOP to BOTTOM,
	vector x from TOP to BOTTOM.
    """
    AT, \
    AB  = flame.part_2x1(A, \
                         0, 'TOP')

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'TOP')

    while AT.shape[0] < A.shape[0]:

        A0,  \
        a1t, \
        A2   = flame.repart_2x1_to_3x1(AT, \
                                       AB, \
                                       1, 'BOTTOM')

        x0,   \
        chi1, \
        x2    = flame.repart_2x1_to_3x1(xT, \
                                        xB, \
                                        1, 'BOTTOM')

        laff.axpy( chi1, a1t, y )

        AT, \
        AB  = flame.cont_with_3x1_to_2x1(A0,  \
                                         a1t, \
                                         A2,  \
                                         'TOP')

        xT, \
        xB  = flame.cont_with_3x1_to_2x1(x0,   \
                                         chi1, \
                                         x2,   \
                                         'TOP')



