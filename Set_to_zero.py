# Programmed by: jasdev

import flame
import laff as laff

def Set_to_zero_unb_var1(A):

    AL, AR = flame.part_1x2(A, \
                            0, 'LEFT')

    while AL.shape[1] < A.shape[1]:

        A0, a1, A2 = flame.repart_1x2_to_1x3(AL, AR, \
                                             1, 'RIGHT')

        #------------------------------------------------------------#

        laff.zerov(a1)
        

        #------------------------------------------------------------#

        AL, AR = flame.cont_with_1x3_to_1x2(A0, a1, A2, \
                                            'LEFT')

    flame.merge_1x2(AL, AR, A)

