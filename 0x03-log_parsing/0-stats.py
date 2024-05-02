#!/usr/bin/python3
"""print data"""
from sys import stdin

def print_statistics(total_size, status_counts):
    print("Total file size:", total_size)
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")

def main():
    line_count = 0
    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in stdin:
            line_count += 1

            # Split line and handle errors
            try:
                parts = line.split()
                file_size += int(parts[-1])
                status_code = int(parts[-2])
            except (ValueError, IndexError):
                continue  # Skip lines with incorrect format

            if status_code in status_codes:
                status_codes[status_code] += 1

            if line_count == 10:
                print_statistics(file_size, status_codes)
                # Reset counters
                line_count = 0
                file_size = 0
                status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)

