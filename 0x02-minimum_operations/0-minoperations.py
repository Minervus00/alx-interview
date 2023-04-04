#!/usr/bin/python3
"""Module containing the minOperations function

Explanations:
Only two operations are available: 'Copy All' and 'Paste'
Given that, at each step we have two choices to get a result:
- (A) 'Copy All' and 'Paste' => (2 operations) and (buffer_content = content
&& content *= 2)
- (B) 'Paste' => (a single operation) and (content += buffer_content)

We can then draw a binary tree for all possible events where each node is
the number of H we actually have. So, 1 (initial state) will be the root and
it's only child is 2 (the first step is always A). Then if we choose (A) we'll
have 4 and (B) will result 3. By reasoning between (A) and (B) for each new
child we'll draw our binary tree.

With a deep look to this binary tree, given the wanted 'n' we can find the
sortest path and with more analysis, this path follows this algorithm starting
from the root node:
1) If the current node is n, done !!
2) Else if it is a multiple of n: choose path (A) => go to 1)
2) Else (not a multiple of n ): choose path (B) => go to 1)

This algorithm is used in the minOperations function
"""


def minOperations(n):
    """ Returns the fewest number of operations needed to result in exactly
        n H characters in the file.
    """
    if int(n) != n or n <= 1:
        return 0
    ops = 0
    curr_nh = 1
    buff = 1
    while curr_nh != n:
        if n % curr_nh == 0:
            ops += 2
            buff = curr_nh
            curr_nh *= 2
        else:
            ops += 1
            curr_nh += buff
    return ops
