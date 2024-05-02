#!/usr/bin/python3
"""print statistics"""
from sys import stdin


def printstats(file_size, status_codes):
    """
    This prints statistics at the beginning and every 10 lines
    This will also be called on a Keyboard interruption
    """
    print(f"File size: {file_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


line_count = 0
file_size = 0
status_code = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for line in stdin:
        line_count += 1
        split_line = line.split()

        if len(split_line) > 1:
            file_size += int(split_line[-1])

        if len(split_line) > 2 and split_line[-2].isnumeric():
            status_code = split_line[-2]
        else:
            status_code = 0

        if status_code in status_codes.keys():
            status_codes[status_code] += 1

        if line_count == 10:
            printstats(file_size, status_codes)

    printstats(file_size, status_codes)

except (KeyboardInterrupt):
    printstats(file_size, status_codes)
