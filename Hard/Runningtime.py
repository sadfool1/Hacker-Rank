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


#A = np.array([i* random.randint(2,pow(10,2)) for i in range(1, pow(10,2))])
#B = np.array([i* random.randint(2,pow(10,2)) for i in range(1, pow(10,2))])

#print (A,B)
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
    
    A_factor = [] #initialise 
    B_factor = []  #initialise 
    
    for i in range(1, math.ceil(math.sqrt(Ai)) + 1):
        if Ai % i == 0:
            A_factor.append(i)
            A_factor.append(Ai/i)
            #APPEND THE FACTORS
            
    for i in range(1, math.ceil(math.sqrt(Bj))+ 1):
        if Bj % i ==0:
            B_factor.append(i)
            B_factor.append(Bj/i)
            
    
    for i in range(len(A_factor)):
        for j in range(len(B_factor)):
            if A_factor[i] == B_factor[j]:
                factor_counter = factor_counter + 1
                
    if factor_counter > 1:
        return False
    else:

        return True

coprime_checker(32,32)
    
A = np.array([3, 7, 32])
B = np.array([6, 14, 15])

def main(A, B):
    
    tempi = []
    tempj = []
    
    for i in range(0,len(A)):
        for j in range(0,len(B)):
            #print ("i = %d j = %d." % (i,j), end = '')
            
            if coprime_checker(int(A[i]), int(B[j])) == True:
                pass
            
            else:
                #print ("Deleting %d & %d" %(A[i], B[j]), end = '')
                
                tempi.append(i)
                tempj.append(j)
                
                break
                
    deleter(A, B, tempi[0],tempj[0])
    

def deleter(A, B, a,b):
    global counter

    try:
        counter = counter + 1
        
        A = np.delete(A, a, axis  = 0)
        B = np.delete(B, b, axis  = 0)
        
        main(A, B) #now iterate the new arrays
        
    except IndexError: #signal it is over
        print ("The total Counter for this method = %d." % counter)
        
main(A, B) #initiliase the code
