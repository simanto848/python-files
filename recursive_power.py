"""
Created on Wed May 29 16:45:15 2024

@author: Simanto
"""

def sumOfDigits(n):
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n / 10))

sum = sumOfDigits(121)
print(sum)