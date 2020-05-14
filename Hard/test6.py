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


#A = np.array([i* random.randint(2,10**9) for i in range(1, 10**5+1)])
#B = np.array([i* random.randint(2,10**9) for i in range(1, 10**5+1)])



counter = 0



def coprime_checker (Ai, Bj):
    
    global counter
    
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
    
 



"""        
A = np.array([2,13,12,14,23, 2, 412, 15,4])
A.shape = (len(A),1)
B = np.array([2,13,12,14,23, 2, 412, 15,4])
B.shape = (len(B),1)


A = np.delete(A, 0)

print (A)
"""

A = np.array([2,13,12,14,23, 2, 412, 15,4])

B = np.array([2,13,12,14,23, 2, 412, 15,4])

"""
x = True

while x == True:
    for i in range(A.shape[0]):
        for j in range(B.shape[0]):
            print (A[i],B[j])
            if coprime_checker(A[i], B[i]) == False:
                
                #print (i,j)
                A = np.delete(A,i, axis =0)
                B = np.delete(B,j, axis = 0)
            else:
                counter = counter + 1

print ("The maximum number of times this happens is %d." % counter)
"""

def main():
    global counter
    global A
    global B
    
    for i in range(0,len(A)):
        print ("i = %d"%i)
        
        for j in range(0,len(B)):
            print ("j = %d"%j)
            
            if coprime_checker(int(A[i]), int(B[j])) == True:
                
                print ("ping")
                print (A[i], B[j])

                time.sleep(1)
                
                
            else:
                print ("no ping")
                print (A,B)
                
                A = np.delete(A,i)
                B = np.delete(B,j)
                
                i = i - 1
                j = j - 1
                
                
                print (A,B)
                counter = counter + 1
                

    
   # except IndexError:
        #print ("The maximum number of times this happens is %d." % counter)

        
                
    
main()

#print (len(B))

#coprime_checker(int, int(j))