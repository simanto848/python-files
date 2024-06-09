"""
Created on Wed May 29 16:50:02 2024

@author: Simanto
"""

def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base;
    else:
        return base * power(base, exp - 1)
    
result = power(2, 3)

print(result)