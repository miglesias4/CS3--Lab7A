# -*- coding: utf-8 -*-
"""
Matthew Iglesias
80591632
Diego Aguirre 
T.A. Anitha Nath
"""

def edit_distance(word1, word2):
    w1 = len(word1) + 1
    w2 = len(word2) + 1

    table = {} ##Establishes 2D array
    for i in range(w1): ##Creates "slots" for word 1
        table[i,0]= i
    for j in range(w2): ##Creates "slots" for word 2
        table[0,j]= j
    for i in range(1, w1): ##Fills in 2D array
        for j in range(1, w2):
            if word1[i-1] == word2[j-1]: ##If both letters equal then cost will be 0
                e_distance = 0
            else:
                e_distance = 1
            
            ##Takes the most min value and adds 1 and fills it to current slot
            table[i,j] = min(table[i,j-1] + 1, table[i-1,j] + 1, table[i-1,j-1] + e_distance)

    return table[i,j]

word1 = input("Enter your first word:")
word2 = input("Enter your second word:")

print("Edit distance: ", edit_distance(word1, word2))