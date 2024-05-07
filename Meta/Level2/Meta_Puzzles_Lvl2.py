#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:26:58 2024

@author: guillaumefoure
"""


from typing import List
from collections import Counter


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    """
    Director of Photography
    """
    ########
    ## First version
    
    ## Take note of the positions of each photographs, actors and backdrops
    
    # photographers = []
    # actors = []
    # backdrops = []
    
    # for i in range(len(C)):
    #     if C[i] == "P":
    #         photographers.append(i)
    #     elif C[i] == "A":
    #         actors.append(i)
    #     elif C[i] == "B":
    #         backdrops.append(i)
    
    # artistic = 0
    # # PAB
    # for P in photographers:
    #     for A in actors:
    #         if A - P < 0:
    #             next
    #         if (A - P >= X) and (A - P <= Y):
    #             for B in backdrops:
    #                 if B - A < 0:
    #                     next
    #                 if (B - A >= X) and (B - A <= Y):
    #                     artistic +=1
    
    # # BAP
    # for B in backdrops:
    #     for A in actors:
    #         if A - B < 0:
    #             next
    #         if (A - B >= X) and (A - B <= Y):
    #             for P in photographers:
    #                 if P - A < 0:
    #                     next
    #                 if (P - A >= X) and (P - A <= Y):
    #                     artistic +=1
    
    # print("True: ")
    # print(artistic)
    # print("")
    
    #########
    ## Second version
    
    # Want to count the Ps and Bs at the same time
    # Count the nb of photographs, actors and backdrops
    
    Ps = [0] # nb of P on the left of the index, initiate to 0 for index -1
    Bs = [0] # nb og B on the left of the index
    
    artistic = 0
    
    for c in C:
        if c == "P":
            Ps.append(Ps[-1]+1) # add on P to previous value
            Bs.append(Bs[-1]) # keep same nb of B
        elif c == "B":
            Bs.append(Bs[-1]+1)
            Ps.append(Ps[-1])
        else:
            Ps.append(Ps[-1])
            Bs.append(Bs[-1])
    
    # Remove index -1
    
    Ps = Ps[1:]
    Bs = Bs[1:]
    # print(list(C))
    # print(Ps)
    # print(Bs)
    for i in range(X, len(C)-X+1):
        # print("\ni: {}".format(i))
        c = C[i]
        if c == "A":
            ## PAB
            # print("\n PAB")
            # t = [" "]*len(C)
            # t[i-X] = "X"
            nb_good_P_left = Ps[i-X]
            if i-Y-1 >= 0:
                nb_good_P_left -= Ps[i-Y-1]
                # t[i-Y-1] = "Y"
            
            # print("\nP left:")
            # print(list(C))
            # print([str(Ps[i]) for i in range(len(Ps))])
            # print(t)
            
            # t = [" "]*len(C)
            
            if i+Y > len(C)-1:
                nb_good_B_right = Bs[-1]
                # t[-1] = "Y"
            else:
                nb_good_B_right = Bs[i+Y]
                # t[i+Y] = "Y"
                
            if i+X-1 < len(C):
                nb_good_B_right -= Bs[i+X-1]
                # t[i+X-1] = "X"

            # print("\nB right:")
            # print(list(C))
            # print([str(Bs[i]) for i in range(len(Bs))])
            # print(t)
            
            artistic += nb_good_P_left * nb_good_B_right
            
            # print("P: {}, B: {}".format(nb_good_P_left, nb_good_B_right))
            # print(artistic)
            
            ## BAP
            # print("\n BAP")
            # t = [" "]*len(C)
            
            if i+Y > len(C)-1:
                nb_good_P_right = Ps[-1]
                # t[-1] = "Y"
            else:
                nb_good_P_right = Ps[i+Y]
                # t[i+Y] = "Y"
                
            if i+X-1 < len(C):
                nb_good_P_right -= Ps[i+X-1]
                # t[i+X-1] = "X"

            # print("\nP right:")
            # print(list(C))
            # print([str(Ps[i]) for i in range(len(Ps))])
            # print(t)

            # t = [" "]*len(C)
            # t[i-X] = "X"
            nb_good_B_left = Bs[i-X]
            if i-Y-1 >= 0:
                nb_good_B_left -= Bs[i-Y-1]
                # t[i-Y-1] = "Y"
            
            # print("\nB left:")
            # print(list(C))
            # print([str(Bs[i]) for i in range(len(Bs))])
            # print(t)
            
            
            artistic += nb_good_P_right * nb_good_B_left
            # print("B {}, P: {}".format(nb_good_B_left, nb_good_P_right))
            # print(artistic)
    
    # print(artistic)
    return artistic


def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    """
    Hops
    """
    P.sort()
    
    def getGroupToClosestFriend(i, n, j):
        """
        i+n<j
        """
        return (j-1)-(i+n-1)
    
    if len(P) == 1:
        total = N-P[0]
    else:
        total = 0
        
        f=1 #frog group size
        index_group = P[0]
        # print("i: {}, n: {}, t: {}\n".format(index_group, f, total))
        for i in range(1, len(P)):
            # print(i)
            # print("{}, {}".format(P[i-1], P[i]))
            if P[i]-P[i-1] > 1: #space in between
                total += getGroupToClosestFriend(index_group, f, P[i])
                f += 1 #adding to the frog group
                index_group=P[i]-f+1 #move next to the frog in i
                
            else: #the group gets larger!
                f+=1
            # print("i: {}, n: {}, t: {}\n".format(index_group, f, total))
            
        #All frogs are together > move thee groupe next to N, and f move to go
        total += getGroupToClosestFriend(index_group, f, N) + f
        # print("i: {}, n: {}, t: {}\n".format(index_group, f, total))
    return total


