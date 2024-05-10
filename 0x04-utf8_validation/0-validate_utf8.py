#!/usr/bin/python3
"""
A function that checks if a data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Return true if data is valid."""
    count = 0
    for byte in data:
        if count == 0:
            if (byte & 0b10000000) == 0:
                continue
            elif (byte & 0b11100000) == 0b11000000:
                count = 1
            elif (byte & 0b11110000) == 0b11100000:
                count = 2
            elif (byte & 0b11111000) == 0b11110000:
                count = 3

            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            count -= 1
    return count == 0
