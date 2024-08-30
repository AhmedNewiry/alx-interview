#!/usr/bin/python3
""" N Queens Algorithm with Backtracking """
import sys


class NQueen:
    """Class for solving the N Queens problem using backtracking."""

    def __init__(self, n):
        """Initialize the N-Queens solver.

        Args:
            n (int): The size of the chessboard
            (N x N) and the number of queens.
        """
        self.n = n
        # Board to store queen positions (1-based index)
        self.board = [0] * (n + 1)
        self.solutions = []

    def is_valid(self, k, i):
        """Check if placing a queen at position (k, i) is valid.

        Args:
            k (int): The row in which to place the queen.
            i (int): The column in which to place the queen.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        for j in range(1, k):
            if (self.board[j] == i or  # Same column
                    abs(self.board[j] - i) == abs(j - k)):  # Same diagonal
                return False
        return True

    def solve(self, k):
        """Solve the N Queens problem by placing queens on the board.

        Args:
            k (int): The current row in which to place the next queen.

        Returns:
            list: A list of solutions, where each
            solution is a list of queen positions.
        """
        for i in range(1, self.n + 1):
            if self.is_valid(k, i):
                self.board[k] = i
                if k == self.n:
                    solution = [[row - 1, self.board[row] - 1]
                                for row in range(1, self.n + 1)]
                    self.solutions.append(solution)
                else:
                    self.solve(k + 1)
        return self.solutions


def main():
    """Main function to handle command-line
    arguments and print N Queens solutions."""
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

    nqueen = NQueen(n)
    solutions = nqueen.solve(1)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
