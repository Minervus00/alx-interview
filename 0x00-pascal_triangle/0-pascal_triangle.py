#!/usr/bin/python3
"""Module containing pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal's triangle of n"""
    if n <= 0:
        return []
    psc = []
    for i in range(n):
        if i == 0:
            psc.append([1])
            continue
        tmp = [1]
        length = len(psc[-1])
        for h in range(length):
            x = psc[-1][h]
            if h < length - 1:
                x += psc[-1][h + 1]
            tmp.append(x)
        psc.append(tmp[:])
    return psc
