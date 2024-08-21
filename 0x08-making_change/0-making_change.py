#!/usr/bin/python3
"""Change making module with dynamic programming"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values
    - Uses dynamic programming to ensure optimal solution
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    coins_count = 0
    rem = total

    for coin in sorted_coins:
        if rem == 0:
            break
        if coin <= rem:
            num_coins = rem // coin
            rem -= num_coins * coin
            coins_count += num_coins
    if rem != 0:
        return -1
    return coins_count
