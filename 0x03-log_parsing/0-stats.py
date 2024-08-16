#!/usr/bin/python3
"""
This module reads log lines from stdin, calculates metrics, and outputs
statistics after every 10 lines or when interrupted by a keyboard
"""

import sys


def print_stats(total_size, status_counts):
    """
    Prints the accumulated statistics:

    Args:
        total_size (int): The total file size accumulated.
        status_counts (dict): A dictionary with status codes as keys and their counts as values.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def log_parser():
    """
    Parses the log lines from stdin and computes the required metrics.
    """
    total_size = 0
    status_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 9:
                continue

            # Extract file size
            try:
                file_size = int(parts[-1])
                total_size += file_size
            except ValueError:
                continue

            # Extract status code
            try:
                status_code = int(parts[-2])
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except ValueError:
                continue

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    log_parser()
