# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import sys

import numpy as np
import random

def computerGame(a, b):
    #
    # Write your code here.
    #
    pass


try:
    
    if __name__ == '__main__':
        
        A = np.array([i* random.randint(2,10**9) for i in range(1, 10**5+1)])
        B = np.array([i* random.randint(2,10**9) for i in range(1, 10**5+1)])
    
        n = int(input())
    
        a = list(map(int, input().rstrip().split()))
    
        b = list(map(int, input().rstrip().split()))
    
        result = computerGame(a, b)
    
    

except ValueError:
    print ("Make sure n is a valid integer.")
    