#!/usr/bin/python3
"""
    A method that calculates the fewest
    number of operations needed to result in
    exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
        prototype: def minOperations(n)
        Return: number of min operations
        if n is impossible to achieve, return 0
    """
    now = 1
    start = 0
    count_operations = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            count_operations += 2
        else:
            now += start
            count_operations += 1
    if now != n:
        return 0
    return count_operations
