#!/usr/bin/python3
""" A script to determines if a given data
    set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else return False.
    """
    for num in data:
        if num < 0 or num > 255:
            return False
    try:
        bytes_data = bytes(data)
        bytes_data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
