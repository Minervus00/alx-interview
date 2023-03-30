#!/usr/bin/python3
""" This function checks if all box in boxes can be opened.
    The first box is already opened. All boxes contains numbered
    keys. Each key can unlock box with the same number (from 0 to n-1)
"""


def canUnlockAll(boxes):
    """Boxes is a list of lists(each internal list stands for a box)"""
    n = len(boxes)
    unlocked = [i for i in range(n)]
    keys = [0]
    while(keys and unlocked):
        curr_key = keys.pop(0)
        if curr_key < n and curr_key in unlocked:
            unlocked.remove(curr_key)
            box = boxes[curr_key]
            keys.extend(box)

    return unlocked == []
