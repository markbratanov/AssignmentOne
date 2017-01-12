"""
COP4533
12/01/2017
@author: Mark Bratanov

This file contains the method
which is found in python library
and should calculate gcd faster
"""

import math

def gcd(a=None, b=None):

    if a is None:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

    return math.gcd(a, b)

"""
def main():
    print(gcd())

main()
"""

