# Programmed by: Jasdev SIngh
#                

import flame
import laff as laff

def Tmvmult_ln_unb_var1(L, x, y):
    """
	Tmvmult_ln_unb_var1(matrix, vector, vector)	

	Computes y = L * x + y using DOT products.
	L is the lower triangular matrix.

	Traverses matrix L from TOP-LEFT to BOTTOM-RIGHT,
	vector x from TOP to BOTTOM,
	vector y from TOP to BOTTOM.
    """
    LTL, LTR, \
    LBL, LBR  = flame.part_2x2(L, \
                               0, 0, 'TL')

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'TOP')

    yT, \
    yB  = flame.part_2x1(y, \
                         0, 'TOP')

    while LTL.shape[0] < L.shape[0]:

        L00,  l01,      L02,  \
        l10t, lambda11, l12t, \
        L20,  l21,      L22   = flame.repart_2x2_to_3x3(LTL, LTR, \
                                                        LBL, LBR, \
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

        laff.dots( l10t, x0, psi1 )
        laff.dots( lambda11, chi1, psi1 )

        LTL, LTR, \
        LBL, LBR  = flame.cont_with_3x3_to_2x2(L00,  l01,      L02,  \
                                               l10t, lambda11, l12t, \
                                               L20,  l21,      L22,  \
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

    flame.merge_2x2(LTL, LTR, \
                    LBL, LBR, L)

    flame.merge_2x1(xT, \
                    xB, x)

    flame.merge_2x1(yT, \
                    yB, y)





def Tmvmult_ln_unb_var2(L, x, y):
    """
	Tmvmult_ln_unb_var2(matrix, vector, vector)	

	Computes y = L * x + y using AXPY operations.
	L is the lower triangular matrix.

	Traverses matrix L from TOP-LEFT to BOTTOM-RIGHT,
	vector x from TOP to BOTTOM,
	vector y from TOP to BOTTOM.
    """
    LTL, LTR, \
    LBL, LBR  = flame.part_2x2(L, \
                               0, 0, 'TL')

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'TOP')

    yT, \
    yB  = flame.part_2x1(y, \
                         0, 'TOP')

    while LTL.shape[0] < L.shape[0]:

        L00,  l01,      L02,  \
        l10t, lambda11, l12t, \
        L20,  l21,      L22   = flame.repart_2x2_to_3x3(LTL, LTR, \
                                                        LBL, LBR, \
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

        laff.axpy( chi1, lambda11, psi1 )
        laff.axpy( chi1, l21, y2 )

        LTL, LTR, \
        LBL, LBR  = flame.cont_with_3x3_to_2x2(L00,  l01,      L02,  \
                                               l10t, lambda11, l12t, \
                                               L20,  l21,      L22,  \
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
