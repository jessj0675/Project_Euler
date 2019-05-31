#Project Euler Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#Notes: Natural Number are what you use when you are counting one to one objects.

import numpy as np


def sum3or5below(x):
    sum = 0 
    for x in range(x):
        if(x % 3 == 0) or (x % 5==0):
            sum += x
    return sum
    
if __name__ == "__main__":
    while True:
        x = int(input("Enter Number: "))
        sum  = sum3or5below(x)
        print(sum)