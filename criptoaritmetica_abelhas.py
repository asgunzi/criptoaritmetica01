# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:49:29 2024

@author: asgunzi
"""


for A in range(0,10):
    for B in range(0,10):
        if  A != B:
            for E in range(0,10):
                if  E != A and E != B:
                    for L in range(0,10):
                        if L != A and L != B and L != E:
                            for H in range(0,10):
                                if H != A and H != B and H != E and H != L:
                                    for N in range(0,10):
                                        if N != A and N != B and N != E and N != L and N != H:
                                            for X in range(0,10):
                                                if X != A and X != B and X != E and X != L and X != H and X != N:
                                                    for M in range(0,10):
                                                        if M != A and M != B and M != E and M != L and M != H and M != N  and M != X:
                                                            n1 = A*100_000 + B*10_000 + E*1_000 + L*100 + H*10 + A
                                                            n2 = 100_000*E+ 10_000*N+ 1_000*X + 100*A + 10*M + E
                                                            if 3*int(n1) == int(n2):
                                                                print(n1)
                                                                print(n2)
                                
