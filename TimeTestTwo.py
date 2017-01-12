"""
COP4533
12/01/2017
@author: Mark Bratanov
"""


import timeit, io

a = input('Enter first number: ')
b = input('Enter second number: ')

t = timeit.Timer("EuclidTwo.gcd("+a+", "+b+")", "import EuclidTwo")

results = t.repeat(5, 10000)
for i, item in enumerate(results):
    print(i, "\t", item)
