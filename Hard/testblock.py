#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 22:48:56 2020

@author: jameselijah
"""


import math 
factor_counter = 0
Ai = 17123123
Bj = 12

A_factor = {} #initialise dict
B_factor = {} #initialise dict

for i in range(1, math.ceil(math.sqrt(Ai))):
    if Ai % i == 0:
        A_factor[i] = i
        A_factor[i+1] = Ai/i
        
        
for i in range(1, math.ceil(math.sqrt(Bj))):
    if Bj % i == 0:
        B_factor[i] = i
        B_factor[i+1] = Bj/i

print (A_factor,  B_factor)

for i, j in zip(A_factor, B_factor):
    if factor_counter > 1:
            break
    elif A_factor[i] in B_factor:
        factor_counter = factor_counter + 1
        continue
    else:
        if factor_counter > 1:
            break

print (False if factor_counter > 1 else True)
        



