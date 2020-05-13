# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import sys

import numpy as np
import random

#
# Complete the computerGame function below.
#
def computerGame(a, b):
    #
    # Write your code here.
    #
    pass

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    A = np.array([i* random.randint(2,10**9) for i in range(0, 10**5)])
    B = np.array([i* random.randint(2,10**9) for i in range(0, 10**5)])

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = computerGame(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()