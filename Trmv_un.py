# Programmed by: Jasdev Singh
#                

import flame
import laff as laff

def Trmv_un_unb_var1(U, x):
    """
	Trmv_un_unb_var1(matrix, vector)	

	Computes y = U * x using DOT products.
	U is the upper triangular matrix.

	Traverses matrix U from TOP-LEFT to BOTTOM-RIGHT,
	vector x from TOP to BOTTOM.
    """
    UTL, UTR, \
    UBL, UBR  = flame.part_2x2(U, \
                               0, 0, 'TL')

    xT, \
    xB  = flame.part_2x1(x, \
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

        laff.scal( upsilon11, chi1 )
        laff.dots( u12t, x2, chi1 )

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

    flame.merge_2x1(xT, \
                    xB, x)





def Trmv_un_unb_var2(U, x):
    """
	Trmv_un_unb_var2(matrix, vector)	

	Computes y = U * x using AXPY operations.
	U is the upper triangular matrix.

	Traverses matrix U from TOP-LEFT to BOTTOM-RIGHT,
	vector x from TOP to BOTTOM.
    """
    UTL, UTR, \
    UBL, UBR  = flame.part_2x2(U, \
                               0, 0, 'TL')

    xT, \
    xB  = flame.part_2x1(x, \
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

        laff.axpy( chi1, u01, x0 )
        laff.scal( upsilon11, chi1 )

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

    flame.merge_2x1(xT, \
                    xB, x)

