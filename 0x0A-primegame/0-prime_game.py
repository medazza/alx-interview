#!/usr/bin/python3
"""
Prime game module.
"""

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(nums):
    """
    Counts the number of primes in a given list of numbers.
    """
    primes_count = 0
    for n in nums:
        if is_prime(n):
            primes_count += 1
    return primes_count

def isWinner(x, nums):
    """
    Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    for _ in range(x):
        primes_count = count_primes(nums)
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
        nums.pop(0)
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
