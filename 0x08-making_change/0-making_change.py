#!/usr/bin/python3
"""fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """fewest number of coins needed for change"""
    if total < 1:
        return 0

    coins.sort()
    coins.reverse()

    count = 0

    for coin in coins:
        if total == 0:
            break

        unit_num = total // coin
        count += unit_num
        total -= (unit_num * coin)

    if total == 0:
        return count
    else:
        return -1
