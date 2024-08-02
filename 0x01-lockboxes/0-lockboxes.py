#!/usr/bin/env python3
"""
Module to determine if all boxes can be
unlocked given a list of boxes with keys.
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be unlocked starting from the first box.

    Args:
        boxes (List[List[int]]): A list where each element
        is a list of keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n  # Track which boxes have been unlocked
    unlocked[0] = True  # The first box is unlocked initially
    stack = [0]  # Start with the first box

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
