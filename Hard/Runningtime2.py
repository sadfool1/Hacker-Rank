#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:17:12 2020

@author: jameselijah
"""

import numpy as np
import random
import math
import time


A = np.array([i* random.randint(2,pow(10,5)) for i in range(1, pow(10,3))])
B = np.array([i* random.randint(2,pow(10,5)) for i in range(1, pow(10,3))])

timeinit = time.process_time()

counter = 0

def coprime_checker (Ai, Bj):
    """
    =========================
    Checks Factors of
    Integers then returns
    Boolean if Coprime or not
    =========================
    """
    factor_counter = 0
    
    a = Ai
    b = Bj
    
    A_factor = {} #initialise 
    B_factor = {} #initialise 
    
    for i in range(1, math.ceil(math.sqrt(Ai))):
        if Ai % i == 0:
            A_factor[i] = i
            A_factor[i+1] = Ai/i
            
            #APPEND THE FACTORS
            
    for i in range(1, math.ceil(math.sqrt(Bj))):
        if Bj % i ==0:
            B_factor[i] = i
            B_factor[i+1] = Bj/i
    
    for i in A_factor:
        for j in B_factor:
            if A_factor[i] == B_factor[j]:
                factor_counter = factor_counter + 1
                continue
            else:
                pass
        if factor_counter > 1:
            break
    
    return False if factor_counter > 1 else True


    
#A = np.array([3, 7, 30])
#B = np.array([6, 14, 15])

def main(A, B):
    global counter
    
    tempi = []
    tempj = []
 

    for i in range(0,len(A)):
        if len(tempi) > 1:
            break
        
        for j in range(0,len(B)):
            if coprime_checker(int(A[i]), int(B[j])) == True:
                pass
            else:    
                tempi.append(i)
                tempj.append(j)
                break
        
            

    deleter(A, B, tempi[0],tempj[0])


def deleter(A, B, a,b):
    global counter
    global timeinit

    try:
        counter = counter + 1
        
        A = np.delete(A, a, axis  = 0)
        B = np.delete(B, b, axis  = 0)
        
        main(A, B) #now iterate the new arrays
        
    except IndexError: #signal it is over
        timeend = time.process_time()
        timer =  timeend - timeinit
        print ("The total Counter for this method = %d." % counter)
        print ("Time taken to execute: %f seconds " % timer)


main(A, B) #initiliase the code
