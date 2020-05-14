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


A = np.array([i* random.randint(2,10**3) for i in range(1, 10+1)])
B = np.array([i* random.randint(2,10**3) for i in range(1, 10+1)])

print (A,B)
counter = 0



def coprime_checker (Ai, Bj):
    
    factor_counter = 0
    
    a = Ai
    b = Bj
    
    tempa = [a % i for i in range(1, a+1)]
    
    tempb = [b % i for i in range(1, b+1)]
    
    len_half_A = math.ceil(len(tempa)/2)
    len_half_B = math.ceil(len(tempb)/2)
    
    A_factor = []
    B_factor = []
    
    if a == 2:
        
        if b == 2:
            return False
        
        else:
            
            A_factor = [1, 2]
            
            for i in range(1,len_half_B+1):
                """
                ====================
                Factor finding for B
                ====================
                """
                
                remainder = tempb[i-1] + i
                
                if b % remainder == 0:
                    B_factor.append(remainder)
            
            #print( A_factor, B_factor )
            
            for i in range(len(A_factor)):
                for j in range(len(B_factor)):
                    if A_factor[i] == B_factor[j]:
                        factor_counter = factor_counter + 1
            if factor_counter > 1:
                return False
            else:
                return True
        
    elif b == 2:
        
        B_factor = [1, 2]
        
        for i in range(1,len_half_A+1):
            """
            ====================
            Factor finding for A
            ====================
            """
            
            remainder = tempa[i-1] + i
            
            if a % remainder == 0:
                A_factor.append(remainder)

        #print( A_factor, B_factor )
        
        for i in range(len(A_factor)):
            for j in range(len(B_factor)):
                if A_factor[i] == B_factor[j]:
                    factor_counter = factor_counter + 1
        if factor_counter > 1:
            return False
        else:
    
            return True
    
    else:
        
    
        for i in range(1,len_half_A+1):
            """
            ====================
            Factor finding for A
            ====================
            """
            
            remainder = tempa[i-1] + i
            
            if a % remainder == 0:
                A_factor.append(remainder)
        
        for i in range(1,len_half_B+1):
            """
            ====================
            Factor finding for B
            ====================
            """
            
            remainder = tempb[i-1] + i
            
            if b % remainder == 0:
                B_factor.append(remainder)
                
        
        #print( A_factor, B_factor )
        
        for i in range(len(A_factor)):
            for j in range(len(B_factor)):
                if A_factor[i] == B_factor[j]:
                    factor_counter = factor_counter + 1
        if factor_counter > 1:
            return False
        else:
    
            return True
    

#A = np.array([2, 5, 6, 7])

#B = np.array([4, 9, 10 ,12])


def main(A, B):
    global counter
    global tempi
    global tempj

    #print (len(A),len(B))
    
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
        
        #print ("...DELETED")
        main(A, B)
        
    except IndexError:
        print ("The total Counter for this method = %d." % counter)
        
    
    
main(A, B)

#print (len(B))

#coprime_checker(int, int(j))