#!/usr/bin/python3
""" PRIME GAME """


def is_prime(intg):
    """ Returns True if intg is a prime number False otherwise """
    if intg == 1:
        return False

    primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    root = int(pow(intg, 1/2))
    for y in primes:
        if y > root:
            break
        if intg % y == 0:
            return False
    return True


def sub_primes(n):
    """ Returns the number of primes <= n """
    if n <= 4:
        np = 0
        for y in range(1, n+1):
            if is_prime(y):
                np += 1
    else:
        np = 2
        q = 1
        while 6*q <= n+1:
            if is_prime(6*q - 1):
                np += 1

            if 6*q in [n, n+1]:
                break

            if is_prime(6*q + 1):
                np += 1
            q += 1

    return np


def isWinner(x, nums):
    """ Returns the winner's name """
    won = {'Maria': 0, 'Ben': 0}
    if x != len(nums):
        return None

    for n in nums:
        num_prime = sub_primes(n)
        if num_prime % 2 == 0:
            won['Ben'] += 1
        else:
            won['Maria'] += 1

    # print(won)
    return None if won['Maria'] == won['Ben'] else \
        'Maria' if won['Maria'] > won['Ben'] else 'Ben'
