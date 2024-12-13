#!/usr/bin/python3
"""Module that conatins a function that carries out the prime game
   between Maria and Ben to find the winner.
"""


def is_prime(n: int) -> bool:
    """Checks if an integer is prime"""
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, (n//2 + 1)):
        if n % i == 0:
            return False
    return True


def pick_num(game_num: list, n: int) -> list:
    """Picks a prime number and it's multiples"""
    picked_nums = []
    for num in game_num:
        if is_prime(num):
            for multiplier in range(1, n + 1):
                multiple = num * multiplier
                if multiple > n:
                    break
                if multiple in game_num:
                    picked_nums.append(multiple)
            break
    return picked_nums


def play_round(n: int) -> str:
    """returns the winner after a single round"""
    game_nums = list(range(1, n + 1))
    turn = 1
    if len(game_nums) == 1 and game_nums[0] == 1:
        return "Ben"
    while turn > 0:
        # Maria turn to play
        if turn % 2 != 0:
            picked_nums = pick_num(game_nums, n)
            if not picked_nums:
                return "Ben"
            for num in picked_nums:
                game_nums.remove(num)
        else:
            picked_nums = pick_num(game_nums, n)
            if not picked_nums:
                return "Maria"
            for num in picked_nums:
                game_nums.remove(num)
        turn += 1


def isWinner(x, nums):
    """This simulates the prime game between Maria and Ben.
       Args:
          x: the number of rounds to be played between both players.
          nums: a list of integers defining range of numbers to selcet from
    """
    maria = 0
    ben = 0
    if x > len(nums):
        return None
    if x > 10000 or len(nums) > 10000:
        return None
    for round in range(x):
        if nums[round] < 0:
            return None
        if nums[round] == 0:
            continue
        winner = play_round(nums[round])
        if winner == "Maria":
            maria += 1
        elif winner == "Ben":
            ben += 1
        else:
            return None
    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
