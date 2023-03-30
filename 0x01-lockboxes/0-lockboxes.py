#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [i for i in range(n)]
    keys = [0]
    while(keys):
        curr_key = keys.pop(0)
        if curr_key < n and curr_key in unlocked:
            unlocked.remove(curr_key)
            box = boxes[curr_key]
            keys.extend(box)

    return unlocked == []
