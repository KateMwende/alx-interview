#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed
    to meet a given amount total"""
    if total == 0 or total < 0:
        return 0
    change = 0
    coins = sorted(coins, reverse=True)

    for i in range(len(coins)):
        change += total // coins[i]
        total = total % coins[i]

    if total == 0:
        return change

    return -1
