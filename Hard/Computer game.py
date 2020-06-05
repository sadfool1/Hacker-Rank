#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:17:12 2020

@author: jameselijah

Sophia is playing a game on the computer. There are two random arrays A & B, each having the same number of elements. 
The game begins with Sophia removing a pair (Ai, Bj) from the array if they are not co-prime. She keeps a count on the 
number of times this operation is done.

Sophia wants to find out the maximal number of times(S) she can do this on the arrays. Could you help Sophia find the value?

Input Format

The first line contains an integer n. 2 lines follow, each line containing n numbers separated by a single space. The format is shown below.

Input Format

The first line contains an integer n. 2 lines follow, each line containing n numbers separated by a single space. The format is shown below.

n
A[0] A[1] ... A[n - 1]
B[0] B[1] ... B[n - 1]

Constraints

0 < n <= 105
2 <= A[i], B[i] <= 109
Each element in both arrays are generated randomly between 2 and 109

Output Format

Output S which is the maximum number of times the above operation can be made.

Sample Input
4
2 5 6 7
4 9 10 12
Sample Output

3

Explanation:

You can remove:

(2, 4)
(5, 10)
(6, 9)

hence 3//

"""

import numpy as np
import random
import math
import time


A = np.array([i* random.randint(2,pow(10,5)) for i in range(1, pow(10,2))])
B = np.array([i* random.randint(2,pow(10,5)) for i in range(1, pow(10,2))])

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
    if Ai == Bj:
        return False
    
    factor_counter = 0
    if Ai > 1000 or Bj > 1000:
        return coprime_checker_large_number (Ai, Bj)
        
    A_factor = {} #initialise dict
    B_factor = {} #initialise dict
    
    for i in range(1, Ai+1):
        
        if Ai % i == 0:
            A_factor[i] = i
            
    for i in range(1, Bj+1):
        
        if Bj % i == 0:
            B_factor[i] = i
    
    #print (A_factor,  B_factor)
    
    for i, j in zip(A_factor, B_factor):
        if A_factor[i] == B_factor[j]:
            factor_counter = factor_counter + 1
            continue
        else:
            if factor_counter > 1:
                break
    
    return False if factor_counter > 1 else True

def coprime_checker_large_number (Ai, Bj):

    A_factor = {} #initialise dict
    B_factor = {} #initialise dict
    factor_counter = 0
    
    for i in range(1, math.ceil(math.sqrt(Ai))):
        if Ai % i == 0:
            A_factor[i] = i
            A_factor[i+1] = Ai/i
            
    for i in range(1, math.ceil(math.sqrt(Bj))):
        if Bj % i ==0:
            B_factor[i] = i
            B_factor[i+1] = Bj/i

    for i, j in zip(A_factor, B_factor):
        if factor_counter > 1:
                break
        elif A_factor[i] in B_factor:
            factor_counter = factor_counter + 1
            continue
        else:
            if factor_counter > 1:
                break
    
    return False if factor_counter > 1 else True
    

def main(A, B):
    
    tempi = []
    tempj = []
 

    for i in range(0,len(A)):   
        for j in range(0,len(B)):
            if coprime_checker(int(A[i]), int(B[j])) == True:
                pass
            else:    
                tempi.append(i)
                tempj.append(j)
                break
            
        if len(tempi) > 1:
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
        print ("We are left with these lists A ="+ str(A) + "and B =" + str(B))
        print ("The total Counter for this method = %d." % counter)
        print ("Time taken to execute: %f seconds " % timer)


main(A, B) #initiliase the code
