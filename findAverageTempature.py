"""
Created on Wed May 29 17:01:37 2024

@author: Simanto
"""

def averageTemperature():
    n = int(input("How many day's temperature? "))
    temp= []
    tempSum = 0
    
    if n > 1:
        for i in range(1, n+1):
            x = int(input(f"Day {i}'s temp: "))
            temp.append(x)
            tempSum += x
        
        average = tempSum / len(temp)
        
        print(f"\nAverage = {average}")
        if temp[-1] > temp[-2]:
            print("1 day(s) above average")
        else:
            print("Temperature is normal")
    else:
        print("1 day's temperature can't be average.(Must be greater than or equal")
        
    
averageTemperature()