#!/usr/bin/python3
'''Minimum number of operations
'''

def minOperations(n: int) -> int:
    '''Calculate the minimum number of operations'''
    if n <= 1:
        return 0
    
    current = 1
    holder = 0
    count = 0
    
    while current < n:
        if n % current == 0:
            holder = current
            count += 1
        current += holder
        count += 1

    return count
