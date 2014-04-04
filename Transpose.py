# Programmed by: jasdev
#                

import flame
import laff as laff

def Transpose_unb_var1(A, B):

    AL, AR = flame.part_1x2(A, \
                            0, 'LEFT')

    BT, \
    BB  = flame.part_2x1(B, \
                         0, 'TOP')

    while AL.shape[1] < A.shape[1]:

        A0, a1, A2 = flame.repart_1x2_to_1x3(AL, AR, \
                                             1, 'RIGHT')

        B0,  \
        b1t, \
        B2   = flame.repart_2x1_to_3x1(BT, \
                                       BB, \
                                       1, 'BOTTOM')

        laff.copy( a1, b1t )

        AL, AR = flame.cont_with_1x3_to_1x2(A0, a1, A2, \
                                            'LEFT')

        BT, \
        BB  = flame.cont_with_3x1_to_2x1(B0,  \
                                         b1t, \
                                         B2,  \
                                         'TOP')

    flame.merge_2x1(BT, \
                    BB, B)



def Transpose_unb_var2(A, B):

    AT, \
    AB  = flame.part_2x1(A, \
                         0, 'TOP')

    BL, BR = flame.part_1x2(B, \
                            0, 'LEFT')

    while AT.shape[0] < A.shape[0]:

        A0,  \
        a1t, \
        A2   = flame.repart_2x1_to_3x1(AT, \
                                       AB, \
                                       1, 'BOTTOM')

        B0, b1, B2 = flame.repart_1x2_to_1x3(BL, BR, \
                                             1, 'RIGHT')

        laff.copy( a1t, b1 )
        
        AT, \
        AB  = flame.cont_with_3x1_to_2x1(A0,  \
                                         a1t, \
                                         A2,  \
                                         'TOP')

        BL, BR = flame.cont_with_1x3_to_1x2(B0, b1, B2, \
                                            'LEFT')

    flame.merge_1x2(BL, BR, B)


