#!/usr/bin/python3
"""
Find least no. of operations to achieve 'H' n number of times
"""


def minOperations(n):
    """H should be printed n number of times"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations
