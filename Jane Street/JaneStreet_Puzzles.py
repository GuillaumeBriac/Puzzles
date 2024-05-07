#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:31:21 2024

@author: guillaumefoure
"""
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as patches
import numpy as np
from collections import Counter

grid = [
 ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'D', 'D'],
 ['A', 'E', 'E', 'E', 'B', 'B', 'C', 'D', 'D', 'D', 'F'],
 ['A', 'E', 'E', 'B', 'B', 'B', 'C', 'D', 'D', 'D', 'F'],
 ['A', 'E', 'E', 'B', 'B', 'G', 'G', 'D', 'F', 'F', 'F'],
 ['A', 'E', 'B', 'B', 'D', 'D', 'G', 'D', 'F', 'H', 'F'],
 ['A', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H', 'I'],
 ['J', 'D', 'D', 'D', 'D', 'K', 'K', 'D', 'H', 'H', 'H'],
 ['J', 'J', 'L', 'D', 'L', 'K', 'K', 'D', 'D', 'H', 'D'],
 ['J', 'J', 'L', 'D', 'L', 'K', 'K', 'D', 'D', 'D', 'D'],
 ['J', 'L', 'L', 'J', 'J', 'J', 'K', 'D', 'D', 'D', 'M'],
 ['J', 'J', 'J', 'J', 'J', 'K', 'K', 'K', 'D', 'D', 'M']
 ]

nb_rows = len(grid)
nb_cols = len(grid[0])

# Get the ltters (areas) on ach row
letters_on_row = []
for i in range(nb_rows):
    unique = set()
    for letter in grid[i]:
        unique.add(letter)
    letters_on_row.append(unique)

word_on_row = []
for i in range(nb_rows):
    word = ""
    for j in range(nb_cols):
        word += grid[i][j]
    word_on_row.append(word)


##########

## PLOT

colors = mcolors.TABLEAU_COLORS
c_keys = list(colors.keys())

areas = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M'
    ]

color_map = {}
n = len(colors)
for i in range(len(areas)):
    area = areas[i]
    color_map[area] = colors[c_keys[i%n]]


## Plot
fig, ax = plt.subplots()
ax.set_xlim([0, len(grid)])
ax.set_ylim([0, len(grid[0])])

n = len(grid)
for j in range(len(grid)):
    for i in range(len(grid[0])):
        #plt.scatter([j],[n-i], color= color_map[grid[i][j]], marker="s", s=10)
        rect = patches.Rectangle((j, n-i-1), width=1, height=1, edgecolor="black", facecolor= color_map[grid[i][j]])
        ax.add_patch(rect)

##########


# Maximum number in the grid (on a row)
max_number = 10**(len((grid[0]))) - 1

def match_number_to_word(word):
    """
    Each char from left to right is matched to the rank of first occurance
        e.g.:
            '99403342'
            '11234425'
            ('9' is the first char, then '9'->'1'
             '4' is thee second different char, then '4'->'2')
    """
    map_nb_to_letter = Counter()
    c = 1
    for j in range(len(word)):
        letter = word[j]
        if map_nb_to_letter[letter] == 0:
            map_nb_to_letter[letter] = str(c)
            c += 1 # next letter number
    for letter in map_nb_to_letter.keys():
        word = word.replace(letter, map_nb_to_letter[letter])
    return word


def get_possible_values_fun(row, fun):
    """
    Gets all possible squares that can fit,
    and their possible index in the grid.
    
    Match the string(square number) to a new string.
    Each number from left to right is matched to the rank of first occurance
        e.g.:
            '99403342'
            '11234425'
    See if it could fit in the chosen row regarding the area names, match areas
    with the number.
    """
    
    possibles = {}
    # sizes = {}
    i = 0
    s = 0
    while s < max_number:
        i += 1
        s = fun(i)
        is_added = False #square number not added yet in the possible values
        str_s = str(s)
        
        size = len(str_s)
        if size < 2: #must have at least 2 digits
            next
        
        else:
            for j in range(len(word_on_row[row])-len(str_s)):
                word = word_on_row[row][j: j+len(str_s)]
                match_word = match_number_to_word(word)
                match_s = match_number_to_word(str_s)
        
                if match_word == match_s:
                    if not is_added:
                        possibles[s] = [j]
                        is_added = True
                    else:
                        possibles[s].append(j)
                    
                    # if not size in sizes.keys():
                    #     sizes[size] = (set(), set()) # (indexes, vals)
                        
                    # sizes[size][0].add(j)
                    # sizes[size][1].add(s)

                else:
                    next
            
    return possibles #, sizes

def fibo(max_number):
    fibo = [13, 21] #first two with at least 2 digits
    while fibo[-1] < max_number:
        fibo.append(fibo[-1] + fibo[-2])
    return fibo

def multiples_7(max_number):
    multiples = [14] #first multiple of 7 with at least 2 digits
    i = 3
    while multiples[-1] < max_number:
        multiples.append(7 * i)
        i += 1
    return multiples

# def get_prime_to_prime():
#     primes = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97


def get_possible_values_list(row, full_list):
    possibles = {}
    #sizes = {}
    for val in full_list:
        is_added = False
        str_val = str(val)
        #size = len(str_val)
        for j in range(len(word_on_row[row])-len(str_val)):
            word = word_on_row[row][j: j+len(str_val)]
            match_word = match_number_to_word(word)
            match_val = match_number_to_word(str_val)
    
            if match_word == match_val:
                if not is_added:
                    possibles[val] = [j]
                    is_added = True
                else:
                    possibles[val].append(j)
                
                # if not size in sizes.keys():
                #     sizes[size] = (set(), set()) # (indexes, vals)
                    
                # sizes[size][0].add(j)
                # sizes[size][1].add(val)
            else:
                next
    return possibles #, sizes

def get_shades(row):
    possibilities = possibilities_by_row[row]
    not_shaded = set()
    
    for nb in possibilities.keys():
        len_n = len(str(nb))
        for index in possibilities[nb]:
            for j in range(len_n):
                not_shaded.add(index+j)
    
    shades = []
    for i in range(nb_cols):
        if i not in not_shaded:
            shades.append(i)
    return(shades)


def check_possibility_to_fill_row(row):
    possibilities = possibilities_by_row[row]
    keys = list(possibilities.keys())
    keys.reverse()
    for nb in keys:
        possible_index = possibilities[nb].copy()
        for index in possibilities[nb]:
            size = len(str(nb))
            if index + size - 1 == nb_cols - 3: #will shade n-2, and n-1 unable to be filled
                possible_index.remove(index)
            if index == 2:
                try:
                    possible_index.remove(2) #can't start on index = 2 (otherwise, 1 is shaded, and can't fill 0)
                except:
                    pass
            
        if len(possible_index) == 0:
            possibilities_by_row[row].pop(nb)
        else:
            possibilities_by_row[row][nb] = possible_index 
        
# def adjust_sizes_to_fill_row(row):
#     possibilities = possibilities_by_row[row]
#     sizes = {}

#     for nb in possibilities.keys():
#         for index in possibilities[nb]:    
#             size = len(str(nb))
#             if not size in sizes.keys():
#                 sizes[size] = (set(), set()) # (indexes, vals)
                
#             sizes[size][0].add(index)
#             sizes[size][1].add(nb)
    
#     sizes_by_row[row] = sizes

def get_index_possible_num(row):
    possibilities = possibilities_by_row[row]
    index_possible_num = {}
    for i in range(nb_cols):
        index_possible_num[i] = []
        for num in possibilities.keys():
            if i in possibilities[num]:
                index_possible_num[i].append(num)
    return index_possible_num

def reduce_possibilities(row):
    check_possibility_to_fill_row(row)
    # adjust_sizes_to_fill_row(row)
    
    index_num = get_index_possible_num(row)

    for i in range(nb_cols):
        # print("i: {}".format(i))
        indexes = index_num[i].copy()
        for num in indexes:
            # print("num: {}".format(num))
            size = len(str(num))
            arrival = i + size + 1
            # print(arrival)
            if arrival < nb_cols:
                if index_num[arrival] == []:
                    index_num[i].remove(num)
                    possibilities_by_row[row][num].remove(i)

    keys = list(possibilities_by_row[row].keys())
    for key in keys:
        if possibilities_by_row[row][key] == []:
            possibilities_by_row[row].pop(key)


possibilities_by_row = {}
# sizes_by_row = {}

square = lambda x: x*x
# possibilities_by_row[0], sizes_by_row[0] = get_possible_values_fun(0, square)
# possibilities_by_row[5], sizes_by_row[5] = get_possible_values_fun(4, square)

# possibilities_by_row[4], sizes_by_row[4] = get_possible_values_list(4, full_list=fibo(max_number))

possibilities_by_row[0] = get_possible_values_fun(0, square)
possibilities_by_row[5] = get_possible_values_fun(4, square)

possibilities_by_row[4] = get_possible_values_list(4, full_list=fibo(max_number))

for row in [0, 4, 5]:
    reduce_possibilities(row)


shades = {
    }

for row in possibilities_by_row.keys():
    shades[row] = get_shades(row)



# thirthy_seven_multi = lambda x: 37*x
# possibilities_by_row[3], sizes_by_row[3] = get_possible_values_fun(3, thirthy_seven_multi)

# heighty_height_multi = lambda x: 88*x
# possibilities_by_row[9], sizes_by_row[9] = get_possible_values_fun(9, heighty_height_multi)




def NumberCross4(grid):
    
    return ()