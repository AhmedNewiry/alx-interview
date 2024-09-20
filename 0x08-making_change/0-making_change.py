#!/usr/bin/python3
"""
This module provides the makeChange function which calculates
"""


def makeChange(coins, total):
    """
    Determines the fewest number of
    coins needed to meet a given total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total >= coin:
            count = total // coin
            coin_count += count
            total -= coin * count
        if total == 0:
            return coin_count
    return -1


# Main function testing
if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
