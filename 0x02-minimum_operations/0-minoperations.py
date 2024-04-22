#!/usr/bin/python3
""" method that calculates the fewest number of operations
needed to result in exactly n H characters in the file."""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    """
    op_count = 0
    current_length = 1
    copy_length = 0

    while current_length < n:
        if n % current_length == 0:
            copy_length = current_length
            op_count += 1

        current_length += copy_length
        op_count += 1

    return op_count
