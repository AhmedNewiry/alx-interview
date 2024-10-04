#!/usr/bin/python3
"""Prime Game Module to determine the
winner after x rounds of the game."""

def isWinner(x, nums):
    """Determines the overall winner of
       the game after x rounds.
    """
    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False

    dp = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        dp[i] = dp[i - 1]
        if primes[i]:
            dp[i] += 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if dp[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
