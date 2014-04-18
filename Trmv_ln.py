# Programmed by: Jasdev Singh
#                

import flame
import laff as laff

def Trmv_ln_unb_var1(L, x):
    """
	Trmv_ln_unb_var1(matrix, vector)	

	Computes y = L * x using DOT products.
	L is the lower triangular matrix.

	Traverses matrix L from BOTTOM-RIGHT to TOP-LEFT,
	vector x from BOTTOM to TOP.
    """
    LTL, LTR, \
    LBL, LBR  = flame.part_2x2(L, \
                               0, 0, 'BR')

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'BOTTOM')

    while LBR.shape[0] < L.shape[0]:

        L00,  l01,      L02,  \
        l10t, lambda11, l12t, \
        L20,  l21,      L22   = flame.repart_2x2_to_3x3(LTL, LTR, \
                                                        LBL, LBR, \
                                                        1, 1, 'TL')

        x0,   \
        chi1, \
        x2    = flame.repart_2x1_to_3x1(xT, \
                                        xB, \
                                        1, 'TOP')

        laff.scal( lambda11, chi1 )
        laff.dots( l10t, x0, chi1 )

        LTL, LTR, \
        LBL, LBR  = flame.cont_with_3x3_to_2x2(L00,  l01,      L02,  \
                                               l10t, lambda11, l12t, \
                                               L20,  l21,      L22,  \
                                               'BR')

        xT, \
        xB  = flame.cont_with_3x1_to_2x1(x0,   \
                                         chi1, \
                                         x2,   \
                                         'BOTTOM')

    flame.merge_2x1(xT, \
                    xB, x)





def Trmv_ln_unb_var2(L, x):
    """
	Trmv_ln_unb_var2(matrix, vector)	

	Computes y = L * x using AXPY operations.
	L is the lower triangular matrix.

	Traverses matrix L from BOTTOM-RIGHT to TOP-LEFT,
	vector x from BOTTOM to TOP.
    """
    LTL, LTR, \
    LBL, LBR  = flame.part_2x2(L, \
                               0, 0, 'BR')

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'BOTTOM')

    while LBR.shape[0] < L.shape[0]:

        L00,  l01,      L02,  \
        l10t, lambda11, l12t, \
        L20,  l21,      L22   = flame.repart_2x2_to_3x3(LTL, LTR, \
                                                        LBL, LBR, \
                                                        1, 1, 'TL')

        x0,   \
        chi1, \
        x2    = flame.repart_2x1_to_3x1(xT, \
                                        xB, \
                                        1, 'TOP')

        laff.axpy( chi1, l21, x2 )
        laff.scal( lambda11, chi1 )
        
        LTL, LTR, \
        LBL, LBR  = flame.cont_with_3x3_to_2x2(L00,  l01,      L02,  \
                                               l10t, lambda11, l12t, \
                                               L20,  l21,      L22,  \
                                               'BR')

        xT, \
        xB  = flame.cont_with_3x1_to_2x1(x0,   \
                                         chi1, \
                                         x2,   \
                                         'BOTTOM')

    flame.merge_2x1(xT, \
                    xB, x)
