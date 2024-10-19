#!/usr/bin/python3
"""
Module that calculates the minimum number of operations
to get exactly `n` H characters using Copy All and Paste operations.
"""


def minOperations(n: int) -> int:
    """
    Determines the minimum number of operations needed to achieve
    exactly n 'H' characters.

    Operations allowed:
    1. Copy All: Copy all characters currently in the buffer.
    2. Paste: Paste the copied characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations, or 0 if it's impossible.
    """
    if n < 2:
        return 0

    operations = 0
    current_length = 1
    buffer = 1

    while current_length < n:
        if n % current_length == 0:
            # Perform 'Copy All' and 'Paste'
            buffer = current_length
            operations += 2
            current_length += buffer
        else:
            # Perform 'Paste'
            operations += 1
            current_length += buffer

    return operations if current_length == n else 0
