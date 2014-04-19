# Programmed by: Jasdev Singh
#                

import flame
import laff as laff

def Tmvmult_ut_unb_var1(U, x, y):
    """
	Tmvmult_ut_unb_var1(matrix, vector, vector)	

	Computes y = U' * x + y using DOT products.

	Traverses matrix A from TOP-LEFT to BOTTOM-RIGHT,
	vector x from TOP to BOTTOM,
	vector y from TOP to BOTTOM.
    """
    UTL, UTR, \
    UBL, UBR  = flame.part_2x2(U, \
                               0, 0, 'TL')

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'TOP')

    yT, \
    yB  = flame.part_2x1(y, \
                         0, 'TOP')

    while UTL.shape[0] < U.shape[0]:

        U00,  u01,       U02,  \
        u10t, upsilon11, u12t, \
        U20,  u21,       U22   = flame.repart_2x2_to_3x3(UTL, UTR, \
                                                         UBL, UBR, \
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

        laff.dots( upsilon11, chi1, psi1 )
        laff.dots( u01, x0, psi1 )

        UTL, UTR, \
        UBL, UBR  = flame.cont_with_3x3_to_2x2(U00,  u01,       U02,  \
                                               u10t, upsilon11, u12t, \
                                               U20,  u21,       U22,  \
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





def Tmvmult_ut_unb_var2(U, x, y):
    """
	Tmvmult_ut_unb_var2(matrix, vector, vector)	

	Computes y = U' * x + y using AXPY operations.

	Traverses matrix A from TOP-LEFT to BOTTOM-RIGHT,
	vector x from TOP to BOTTOM,
	vector y from TOP to BOTTOM.
    """
    UTL, UTR, \
    UBL, UBR  = flame.part_2x2(U, \
                               0, 0, 'TL')

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'TOP')

    yT, \
    yB  = flame.part_2x1(y, \
                         0, 'TOP')

    while UTL.shape[0] < U.shape[0]:

        U00,  u01,       U02,  \
        u10t, upsilon11, u12t, \
        U20,  u21,       U22   = flame.repart_2x2_to_3x3(UTL, UTR, \
                                                         UBL, UBR, \
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

        laff.axpy( chi1, u12t, y2 )
        laff.axpy( chi1, upsilon11, psi1 )

        UTL, UTR, \
        UBL, UBR  = flame.cont_with_3x3_to_2x2(U00,  u01,       U02,  \
                                               u10t, upsilon11, u12t, \
                                               U20,  u21,       U22,  \
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
    
