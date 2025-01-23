#!/usr/bin/python3
"""Parses a log file from stdin following a given format"""

import sys
from datetime import datetime


def validate_line(line):
    """Validates the give string adheres toprovided parsing format."""

    try:
        ip_addr, remainder = line.split(' ', 1)
        excess, remainder = remainder.split('[', 1)
        date_str, remainder = remainder.split(']', 1)
        excess, remainder = remainder.split('"', 1)
        url_given, remainder = remainder.split('"', 1)
        status, file_size = remainder.strip().split(' ')
    except Exception:
        return False

    for num in ip_addr.split('.'):
        try:
            int(num)
        except Exception:
            return False
    try:
        datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    except Exception:
        return False
    if url_given != "GET /projects/260 HTTP/1.1":
        return False
    try:
        int(status)
    except Exception:
        return False
    try:
        file_sz = int(file_size)
    except Exception:
        return False
    return (status, file_sz)


def print_stat(file_size, my_status):
    """ Prints the log statistics."""
    print(f"File size: {file_size}")
    for key, value in my_status.items():
        if value > 0:
            print(f"{key}: {value}")


read_lines = 0
total_file_size = 0
my_status = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
}
try:
    for line in sys.stdin:
        read_lines += 1
        line.strip()
        if not validate_line(line):
            continue
        status, file_size = validate_line(line)
        total_file_size += file_size
        for key in my_status.keys():
            if status == key:
                my_status[key] += 1
                break
        if read_lines % 10 == 0:
            print_stat(total_file_size, my_status)
    print_stat(total_file_size, my_status)
except KeyboardInterrupt:
    print_stat(total_file_size, my_status)
