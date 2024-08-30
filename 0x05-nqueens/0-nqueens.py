#!/usr/bin/python3
"""
Solves the N Queens puzzle by placing N queens on an N×N
chessboard such that no two queens attack each other.
"""

import sys


def print_solutions(solutions):
    """Prints each solution in the format required."""
    for solution in solutions:
        print(solution)


def is_not_under_attack(board, row, col):
    """Check if a queen can be placed at (row, col) without being attacked."""
    for r in range(row):
        if board[r] == col or \
           board[r] - col == r - row or \
           board[r] - col == row - r:
            return False
    return True


def solve_nqueens(n):
    """Solve the N Queens problem and return all solutions."""
    solutions = []
    board = [-1] * n

    def backtrack(row):
        if row == n:
            solutions.append([[r, board[r]] for r in range(n)])
            return
        for col in range(n):
            if is_not_under_attack(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
