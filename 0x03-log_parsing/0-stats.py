#!/usr/bin/python3
"""
This script reads log data from stdin, computes metrics including total file size
and counts of HTTP status codes. It prints the statistics after every 10 lines
or upon keyboard interruption (CTRL + C).

Usage:
    ./0-generator.py | ./0-stats.py
"""

import sys
import signal
from collections import defaultdict

# Initialize counters and metrics
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
file_size_total = 0
status_count = defaultdict(int)
line_count = 0

def print_metrics():
    """
    Prints the accumulated metrics:
        - Total file size
        - Count of each status code that has been encountered.
    """
    print(f"File size: {file_size_total}")
    for status in sorted(status_codes):
        if status_count[status] > 0:
            print(f"{status}: {status_count[status]}")

def signal_handler(sig, frame):
    """
    Handles keyboard interruption (CTRL + C). Prints final statistics and exits.

    Args:
        sig (int): Signal number.
        frame (frame): Current stack frame.
    """
    print("\nKeyboardInterrupt received. Printing final statistics.")
    print_metrics()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

def process_log_lines():
    """
    Reads from stdin line by line, parses the log entries, and computes the metrics.
    Prints the statistics after every 10 lines.
    """
    global file_size_total, status_count, line_count

    # Read from stdin line by line
    for line in sys.stdin:
        line = line.strip()

        # Parse the line
        parts = line.split()
        if len(parts) != 6:
            continue  # Skip lines that do not match the expected format

        try:
            file_size = int(parts[5])
            status_code = int(parts[4])
            if status_code in status_codes:
                file_size_total += file_size
                status_count[status_code] += 1
                line_count += 1
        except ValueError:
            continue  # Skip lines with invalid integers

        # Print metrics after every 10 lines
        if line_count % 10 == 0:
            print_metrics()

if __name__ == "__main__":
    process_log_lines()
