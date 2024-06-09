"""
Created on Wed May 29 16:53:58 2024

@author: Simanto
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

result = gcd(48, 18)

print(result)