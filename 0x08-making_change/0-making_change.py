#!/usr/bin/python3

"""
Making a change from within
"""

def makeChange(coins, total):
    """
     """makeChange function that determines the fewest
    number of coins needed to meet a given amount total.
    """

     Returns:
        number: number of coins needed to meet total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        while total >= coin:
            total -= coin
            count += 1
    if total != 0:
        return -1
    return count
