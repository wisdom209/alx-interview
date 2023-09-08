#!/usr/bin/python3
"""Prime game module"""


def isPrime(num):
    """determine if a number is prime"""
    if num <= 1:
        return False
    if num == 2:
        return True
    for x in range(2, num // 2):
        if num % x == 0:
            return False
    return True


def removeMultiples(num, arr):
    """remove multiples of num in arr"""
    new_arr = []
    for x in arr:
        if x % num != 0:
            new_arr.append(x)
    return new_arr


def find_prime_in_set(arr):
    """find a prime number in set"""
    for num in arr:
        if isPrime(num):
            return num
    return None


def isWinner(numRounds, rounds):
    """Prime game function"""
    maria_wins = 0
    ben_wins = 0
    countRounds = 0

    for round in rounds:
        if countRounds == numRounds:
            break

        countRounds += 1
        count = 0

        round_set = [x for x in range(1, round + 1)]

        while True:
            primeNum = find_prime_in_set(round_set)
            if (primeNum is None):
                break
            round_set = removeMultiples(primeNum, round_set)
            if round_set is None or round_set == []:
                break
            count += 1
        if count != 0 and count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"

    return None
