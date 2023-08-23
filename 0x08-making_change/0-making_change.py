#!/usr/bin/python3
""" Find the number of coins to meet the total """


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet `total`
    + coins: a list of the values of the coins in your possession
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += (total // coin)
        total %= coin
        if total == 0:
            return count
    return -1
