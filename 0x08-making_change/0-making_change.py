#!/usr/bin/python3
"""0. Change comes from within module
"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins required to make the given amount.

    Args:
        coins (list): A list of coin denominations, sorted in descending order.
        amount (int): The target amount to make change for.

    Returns:
        int: The minimum number of coins required to make the given amount, or -1 if it's not possible.
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
