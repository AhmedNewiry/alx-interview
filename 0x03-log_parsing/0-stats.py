#!/usr/bin/python3
"""
log_parser module

This script reads stdin line by line, computes metrics on the logs, and
prints statistics every 10 lines or upon keyboard interruption (CTRL + C).

The expected input format is:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Metrics computed:
- Total file size
- Number of occurrences for each status code

Status codes handled:
200, 301, 400, 401, 403, 404, 405, 500
"""

import sys
import signal

# Initialize metrics
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats():
    """
    Print the accumulated metrics.

    This function prints the total file size and the count of each status code
    in ascending order. Only status codes that have been encountered are printed.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C).

    This function is triggered when a SIGINT signal is received, which typically
    happens when the user presses CTRL + C. It prints the accumulated metrics
    and exits the program.

    Args:
        sig (int): Signal number.
        frame (FrameType): Current stack frame.
    """
    print_stats()
    sys.exit(0)


# Set up the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

line_count = 0

for line in sys.stdin:
    parts = line.split()

    # Skip lines that don't have the expected format
    if len(parts) != 9:
        continue

    ip, _, _, date, _, request, _, status_code, file_size = parts

    # Validate and extract required parts
    if not request.startswith('"GET ') or not request.endswith(' HTTP/1.1"'):
        continue
    if status_code not in status_codes:
        continue

    try:
        file_size = int(file_size)
        total_size += file_size
        status_codes[status_code] += 1
    except ValueError:
        continue

    line_count += 1

    # Print stats after every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print remaining stats if not a multiple of 10 lines
print_stats()
