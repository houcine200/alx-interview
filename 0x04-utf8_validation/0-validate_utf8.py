#!/usr/bin/python3
""" A script to determines if a given data
    set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else return False.
    """
    count = 0

    for byte in data:
        if not 0 <= byte <= 255:
            return False

        if count == 0:
            if byte >> 7 == 0b0:
                return False
            elif byte >> 5 == 0b110:
                count = 1
            elif byte >> 4 == 0b1110:
                count = 2
            elif byte >> 3 == 0b11110:
                count = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                count -= 1
            else:
                return False

    return count == 0
