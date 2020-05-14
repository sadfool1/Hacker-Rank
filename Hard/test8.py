import math
import numpy as np

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
        
print (coprime_checker (2, 1))
    