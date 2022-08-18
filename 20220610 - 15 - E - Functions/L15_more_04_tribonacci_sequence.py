# 20220615 - Python Code - Functions - More Exercise
# 04 - Tribonacci Sequence - judge url: https://judge.softuni.org/Contests/Practice/Index/1729#3


# -------------- version 1 -------------------------- judge 100%


def tribonacci(num):
    output = [1]

    for i in range(1, num):
        output.append(sum(output[-1: -4: -1]))
    return [str(k) for k in output]


num_end = int(input())
result = tribonacci(num_end)

print(' '.join(result))


""" _______________ Tribonacci Sequence __________________


In the Tribonacci sequence, every number is formed by the sum of the previous 3.
Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space,
starting from 1.

You will receive a positive integer number as input.


_________ Test Data ___________


Input 1:
--------
4


Output 1:
--------
1 1 2 4


-------------------------------


Input 2:
-------
8


Output 2:
--------
1 1 2 4 7 13 24 44


-------------------------------
"""
