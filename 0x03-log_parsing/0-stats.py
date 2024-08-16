#!/usr/bin/python3
"""
This module reads log lines from stdin, calculates metrics, and outputs
statistics after every 10 lines or when interrupted by a keyboard
"""

import sys
import signal


total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
line_count = 0


def print_statistics():
    """
    Prints the accumulated statistics:
    - Total file size of all processed lines.
    - Number of occurrences of each HTTP status code, sorted by status code.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """
    Handles the SIGINT signal (usually triggered by CTRL + C).
    Prints the current statistics and exits the program.

    Args:
        sig: The signal number.
        frame: The current stack frame.
    """
    print_statistics()
    sys.exit(0)


# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        ip_address = parts[0]
        date = parts[3] + " " + parts[4]
        method = parts[5]
        url = parts[6]
        protocol = parts[7]
        status_code = parts[8]
        file_size = parts[9]

        if method != '"GET' or protocol != 'HTTP/1.1"':
            continue

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        total_file_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print_statistics()

except Exception as e:
    pass

# Print final statistics after processing all lines
print_statistics()
