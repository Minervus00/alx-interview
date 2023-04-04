#!/usr/bin/env python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

for n in range(16):
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
