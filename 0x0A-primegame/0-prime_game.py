#!/usr/bin/python3
"""Prime Game"""


def count_primes(n):
    """check if one item in list is prime"""
    number = 0
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            number += 1
            for i in range(p, n + 1, p):
                sieve[i] = False
    return number


def isWinner(x, nums):
    """
    Determine the winner after x rounds of the game.
    Maria and Ben take turns picking primes and removing
    them and their multiples from the set.
    """
    players = {"Maria": 0, "Ben": 0}
    for num in nums[:x]:
        count_p = count_primes(num)
        if count_p % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1
    if players['Ben'] > players['Maria']:
        return 'Ben'
    if players['Maria'] > players['Ben']:
        return 'Maria'
    return None
