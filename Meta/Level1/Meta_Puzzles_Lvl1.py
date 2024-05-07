#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:26:58 2024

@author: guillaumefoure
"""


from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    """
    Cafeteria
    Level 1
    """
    
    # We try to put people as close as possible to already seated diners
    additional_diners = 0
    n = len(S)
    S.sort()
    
    # Between seat 1 and 1st occupied
    additional_diners += (S[0]- 1)//(K+1)

    # Between last seat and last occupied
    additional_diners += (N - S[n-1])//(K+1)
    
    for i in range(1, n):
        seats_available = (S[i] - S[i-1])/(K+1)
        additional_diners += int(seats_available) - 1
    
    return additional_diners


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


from typing import List
from collections import Counter


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    """
    Kaitenzushi
    """
    
    ## First idea
    # eaten_dishes = 0

    # previous = []
    # for dish in D:
    #     # if not in the list of previous K dishes: eat it and add to list
    #     if not (dish in previous):
    #         eaten_dishes += 1
    #         previous.append(dish) #add element at the end of the list
    #     if len(previous)==K+1: #the 'queue' is full, remove first element
    #         previous = previous[1:]
    
    ## Second idea
    eaten_dishes = 1 #eat the first dish
    previous = Counter() #previous eaten: counter of the rank of the last time eaten
    previous[D[0]] = 1 #rank in the previous eaten dishes
    
    i = 2 #rank in the previous dishes
    for dish in D:
        val = previous[dish]
        # print("\nprevious: {}, i: {}, dish:{}, val:{}".format(previous, i, dish, val))
        if val>0 and i-val<=K: #already seen dish, and in the K latest
            next
        else:
            eaten_dishes += 1 #eat the dish
            previous[dish] = i #add to previous
            i += 1

    return eaten_dishes

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    """
    Rotary Lock
    """
    
    min_time = 0
    init = 1 #initial value selected
    for c in C:
        # min between:
        # - abs value of the diff between current number and previous (=init)
        # - sum of N minus the highest digit selected (=c) and previous (=init)
        #   plus the min between c and init
        t = min(abs(c-init), (N-max(c, init))+min(c, init))
        min_time += t
        init = c
    return min_time


def getMinProblemCount(N: int, S: List[int]) -> int:
    """
    Scoreboard Inference
    """
    S.sort()
    pb = {1: 0, 2: 0} #nb of problems with score 1 and 2
    for i in range(len(S)):
        #Min 2 pts problems to get this score (maximize the number of twos)
        min_two = S[i]//2
        
        # add problem with score 2 if needed
        if min_two - pb[2] > 0:
            pb[2] += min_two - pb[2]
    
        # add problem with 1 score if needed
        pt_needed = S[i] - (pb[1] + pb[2] * 2)
        if pt_needed > 0:
            pb[1] += pt_needed
    
    
    return pb[1] + pb[2]

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  """
  Stack Stabilization
  """
  nb_deflation = 0
  n = len(R)
  for i in range(1, n):
      # from bottom to top
      if R[n-i-1] >= R[n-i]: #if above disc larger, give it size lower one -1
          nb_deflation += 1
          R[n-i-1] = R[n-i]-1

          
  return nb_deflation if R[0] > 0 else -1


def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    
    def getUniformIntegerCount(A: int) -> int:
        
        # A = str(A)
        # n = len(A) - 1
        # count = (n)*9 + max(0, (int(A[0])-1))
        
        # if int(A) == int(A[0]*(n+1)):
        #     count += 1
        
        count = 0
        
        stA = str(A)
        n = len(stA)
        if A < int(stA[0]*n):
            if int(stA[0])>1:
                A = int(stA[0]*n) - 10 ** (n-1)
            else:
                A = 10 ** (n-1) - 1
        
        stA = str(A)
        n = len(stA)
        
        stA = str(min(A, int(stA[0]*n)))
        if int(stA) == int(stA[0]*(n)):
            count += int(stA[0])
        
        count += (n-1)*9
        
        return count
    
    count = getUniformIntegerCount(B) - getUniformIntegerCount(A)
    
    A = str(A)
    n = len(A)
    if int(A) == int(A[0]*n):
        count += 1

    return count
