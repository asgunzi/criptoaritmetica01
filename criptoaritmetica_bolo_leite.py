# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 08:27:40 2024

@author: ASGUNZI
"""


for B in range(0,10):
    for L in range(1,10):
        if L != B:
            for O in range(0,10):
                if O != B and O != L:
                    for C in range(0,10):
                        if C != B and C != L and C != O:
                            for M in range(0,10):
                                if M != B and M != L and M != O and M != C:
                                    for E in range(0,10):
                                        if E != B and E != L and E != O and E != C and E != M:
                                            for I in range(0,10):
                                                if I != B and I != L and I != O and I != C and I != M and I != E:
                                                    for T in range(0,10):
                                                        if T != B and T != L and T != O and T != C and T != M and T != E and T != I:
                                                            bolo = B*1000 + O *100 + L *10 + O
                                                            com =  C *100 + O *10 + M
                                                            leite =  L*10000 + E*1000 + I *100 + T *10 + E
                                                            
                                                            if int(bolo) + int(com) == int(leite):
                                                                print(bolo, com, leite)
                                                        

                                    
    