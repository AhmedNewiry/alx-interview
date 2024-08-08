"""
Module for calculating the minimum number
"""

def minOperations(n):
    """
    Calculate the minimum number of operations to achieve exactly `n`
    'H' characters in a files
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    # Factorize n
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations
