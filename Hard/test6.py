#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:17:12 2020

@author: jameselijah
"""

import numpy as np
import random
import math


#A = np.array([i* random.randint(2,10**9) for i in range(1, 10**5+1)])
#B = np.array([i* random.randint(2,10**9) for i in range(1, 10**5+1)])

A = np.array([2,13,12,14,23, 2, 412, 15,4])

B = np.array([2,13,12,14,23, 2, 412, 15,4])


counter = 0

    
def coprime_checker (Ai, Bj):
    a = Ai
    b = Bj
    
    tempa = [a % i for i in range(1, a+1)]
    
    tempb = [b % i for i in range(1, b+1)]
    
    len_half_A = math.ceil(len(tempb)/2)
    len_half_B = math.ceil(len(tempb)/2)

    A_factor = []
    B_factor = []
    
    for i in range(1,len_half_B+1):
        
        remainder = tempa[i-1] + i
        
        if a % remainder == 0:
            A_factor.append(remainder)
    
    for i in range(1,len_half_A+1):
        
        remainder = tempb[i-1] + i
        
        if b % remainder == 0:
            B_factor.append(remainder)
            
            
    print (A_factor,B_factor)
    
    
    
coprime_checker (3, 2)

def problem(a,b):
    global A
    global B
    global counter
    
    for i in range(len(A)):
        if A[i] == 2:
            for j in range(len(B)):
                if B[j] == 2: #NOT COPRIME
                    counter = counter + 1
                    A = np.delete(A,i)
                    B = np.delete(B,j)
                    pass
                
                elif B[j] % 2 == 0: #NOT COPRIME
                    counter = counter + 1
                    A = np.delete(A,i)
                    B = np.delete(B,j)
                else:
                    coprime_checker(A[i], B[j])
                    
                    
                    
            
        elif A[i] % 2 == 0:
            continue
            
        else:
            for j in range(len(B)):
                if B[j] == 2:
                    if B[j] == 2: #NOT COPRIME
                        counter = counter + 1
                        A = np.delete(A,i)
                        B = np.delete(B,j)
                        pass
                        
                    elif B[j] % 2 == 0: #NOT COPRIME
                        counter = counter + 1
                        A = np.delete(A,i)
                        B = np.delete(B,j)
                #coprime_checker(A[i], B[j])
            
            
    