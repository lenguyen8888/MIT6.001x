# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 18:56:53 2023

@author: ethanle
"""

# The greatest common divisor of two positive integers is the largest integer
# that divides each of them without remainder. For example,

# gcd(2, 12) = 2

# gcd(6, 12) = 6

# gcd(9, 12) = 3

# gcd(17, 12) = 1

# Write an iterative function, gcdIter(a, b), that implements this idea.
# One easy way to do this is to begin with a test value equal to the smaller 
# of the two input arguments, and iteratively reduce this test value by 1 
# until you either reach a case where the test divides both a and b without
# remainder, or you reach 1.

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
        smallVal = a
    else:
        smallVal = b
    for i in range(smallVal, 0, -1):
        if i == 1:
            break
        if a % i == 0 and b % i == 0:
            break
    return i

