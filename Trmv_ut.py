# Programmed by: Jasdev Singh
#                

import flame
import laff as laff

def Trmv_ut_unb_var1(U, x):
    """
	Trmv_ut_unb_var1(matrix, vector)	

	Computes x = U' * x using DOT products.

	Traverses matrix U from BOTTOM-RIGHT to TOP-LEFT,
	vector x from BOTTOM to TOP.
    """
    UTL, UTR, \
    UBL, UBR  = flame.part_2x2(U, \
                               0, 0, 'BR')

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'BOTTOM')

    while UBR.shape[0] < U.shape[0]:

        U00,  u01,       U02,  \
        u10t, upsilon11, u12t, \
        U20,  u21,       U22   = flame.repart_2x2_to_3x3(UTL, UTR, \
                                                         UBL, UBR, \
                                                         1, 1, 'TL')

        x0,   \
        chi1, \
        x2    = flame.repart_2x1_to_3x1(xT, \
                                        xB, \
                                        1, 'TOP')

        laff.scal( upsilon11, chi1 )
        laff.dots( u01, x0, chi1 )
        
        UTL, UTR, \
        UBL, UBR  = flame.cont_with_3x3_to_2x2(U00,  u01,       U02,  \
                                               u10t, upsilon11, u12t, \
                                               U20,  u21,       U22,  \
                                               'BR')

        xT, \
        xB  = flame.cont_with_3x1_to_2x1(x0,   \
                                         chi1, \
                                         x2,   \
                                         'BOTTOM')

    flame.merge_2x1(xT, \
                    xB, x)




def Trmv_ut_unb_var2(U, x):
    """
	Trmv_ut_unb_var2(matrix, vector)	

	Computes x = U' * x using AXPY operations.

	Traverses matrix U from BOTTOM-RIGHT to TOP-LEFT,
	vector x from BOTTOM to TOP.
    """
    UTL, UTR, \
    UBL, UBR  = flame.part_2x2(U, \
                               0, 0, 'BR')

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'BOTTOM')

    while UBR.shape[0] < U.shape[0]:

        U00,  u01,       U02,  \
        u10t, upsilon11, u12t, \
        U20,  u21,       U22   = flame.repart_2x2_to_3x3(UTL, UTR, \
                                                         UBL, UBR, \
                                                         1, 1, 'TL')

        x0,   \
        chi1, \
        x2    = flame.repart_2x1_to_3x1(xT, \
                                        xB, \
                                        1, 'TOP')

        laff.axpy( chi1, u12t, x2 )
        laff.scal( upsilon11, chi1 )
        
        UTL, UTR, \
        UBL, UBR  = flame.cont_with_3x3_to_2x2(U00,  u01,       U02,  \
                                               u10t, upsilon11, u12t, \
                                               U20,  u21,       U22,  \
                                               'BR')

        xT, \
        xB  = flame.cont_with_3x1_to_2x1(x0,   \
                                         chi1, \
                                         x2,   \
                                         'BOTTOM')

    flame.merge_2x1(xT, \
                    xB, x)
