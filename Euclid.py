"""
COP4533
12/01/2017
@author: Mark Bratanov

This file contains the euclid algorithm
which calculates the gcd of the
two numbers passed into the method
"""

import io

def gcd(a=None, b=None):

    if a is None:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

    if b == 0:
        return a
    else:
        return gcd(b, a % b)

"""
def main():
    print(gcd())

main()
"""

