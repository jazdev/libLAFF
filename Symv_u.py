# Programmed by: Jasdev Singh
#                

import flame
import laff as laff

def Symv_u_unb_var1(A, x, y):
    """
	Symv_u_unb_var1(matrix, vector, vector)	

	Computes y = A * x + y using DOT products.

	A is a symmetric matrix.

	Traverses matrix A from TOP-LEFT to BOTTOM-RIGHT,
	vector x from TOP to BOTTOM,
	vector y from TOP to BOTTOM.
    """
    ATL, ATR, \
    ABL, ABR  = flame.part_2x2(A, \
                               0, 0, 'TL')

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'TOP')

    yT, \
    yB  = flame.part_2x1(y, \
                         0, 'TOP')

    while ATL.shape[0] < A.shape[0]:

        A00,  a01,     A02,  \
        a10t, alpha11, a12t, \
        A20,  a21,     A22   = flame.repart_2x2_to_3x3(ATL, ATR, \
                                                       ABL, ABR, \
                                                       1, 1, 'BR')

        x0,   \
        chi1, \
        x2    = flame.repart_2x1_to_3x1(xT, \
                                        xB, \
                                        1, 'BOTTOM')

        y0,   \
        psi1, \
        y2    = flame.repart_2x1_to_3x1(yT, \
                                        yB, \
                                        1, 'BOTTOM')

        laff.dots( a01, x0, psi1 )
        laff.dots( alpha11, chi1, psi1 )
        laff.dots( a12t, x2, psi1 )

        ATL, ATR, \
        ABL, ABR  = flame.cont_with_3x3_to_2x2(A00,  a01,     A02,  \
                                               a10t, alpha11, a12t, \
                                               A20,  a21,     A22,  \
                                               'TL')

        xT, \
        xB  = flame.cont_with_3x1_to_2x1(x0,   \
                                         chi1, \
                                         x2,   \
                                         'TOP')

        yT, \
        yB  = flame.cont_with_3x1_to_2x1(y0,   \
                                         psi1, \
                                         y2,   \
                                         'TOP')

    flame.merge_2x1(yT, \
                    yB, y)






def Symv_u_unb_var2(A, x, y):
    """
	Symv_u_unb_var2(matrix, vector, vector)	

	Computes y = A * x + y using AXPY operations.

	A is a symmetric matrix.

	Traverses matrix A from TOP-LEFT to BOTTOM-RIGHT,
	vector x from TOP to BOTTOM,
	vector y from TOP to BOTTOM.
    """
    ATL, ATR, \
    ABL, ABR  = flame.part_2x2(A, \
                               0, 0, 'TL')

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'TOP')

    yT, \
    yB  = flame.part_2x1(y, \
                         0, 'TOP')

    while ATL.shape[0] < A.shape[0]:

        A00,  a01,     A02,  \
        a10t, alpha11, a12t, \
        A20,  a21,     A22   = flame.repart_2x2_to_3x3(ATL, ATR, \
                                                       ABL, ABR, \
                                                       1, 1, 'BR')

        x0,   \
        chi1, \
        x2    = flame.repart_2x1_to_3x1(xT, \
                                        xB, \
                                        1, 'BOTTOM')

        y0,   \
        psi1, \
        y2    = flame.repart_2x1_to_3x1(yT, \
                                        yB, \
                                        1, 'BOTTOM')

        laff.axpy( chi1, a01, y0 )
        laff.axpy( chi1, alpha11, psi1 )
        laff.axpy( chi1, a12t, y2 )
        

        ATL, ATR, \
        ABL, ABR  = flame.cont_with_3x3_to_2x2(A00,  a01,     A02,  \
                                               a10t, alpha11, a12t, \
                                               A20,  a21,     A22,  \
                                               'TL')

        xT, \
        xB  = flame.cont_with_3x1_to_2x1(x0,   \
                                         chi1, \
                                         x2,   \
                                         'TOP')

        yT, \
        yB  = flame.cont_with_3x1_to_2x1(y0,   \
                                         psi1, \
                                         y2,   \
                                         'TOP')

    flame.merge_2x1(yT, \
                    yB, y)






