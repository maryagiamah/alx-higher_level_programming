#!/usr/bin/python3
"""Parse Line"""
import sys


line_count = 0
file_size = 0

stat_code = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}


def print_stats():
    """print_stats"""

    print(f"File size: {file_size}")
    for code in sorted(stat_code.keys()):
        if stat_code[code] > 0:
            print(f"{code}: {stat_code[code]}")

try:
    for line in sys.stdin:
        parts = line.split()
 
        if len(parts) < 6:
            continue 

        code = parts[-2]
        line_count += 1
        file_size += int(parts[-1])

        if code in stat_code:
            stat_code[code] += 1
        else:
            continue

        if (line_count % 10) == 0:
            print_stats()
except KeyboardInterrupt:
    pass
finally:
    print_stats()
