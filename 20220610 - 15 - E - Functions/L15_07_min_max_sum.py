# 20220614 - Python - Functions - Exercise
# 07 - Mim Max and Sum - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#6


# ------------------- version 2 ----------------------- judge 100%


lst_nums = [int(i) for i in input().split()]
print(f'The minimum number is {min(lst_nums)}')
print(f'The maximum number is {max(lst_nums)}')
print(f'The sum number is: {sum(lst_nums)}')


# ------------------- version 1 ----------------------- judge 100%


def min_max_sum(lst_ints: list):
    min_num = min(lst_ints)
    max_num = max(lst_ints)
    sum_all_nums = sum(lst_ints)

    return f'The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {sum_all_nums}'


lst_nums = [int(i) for i in input().split()]
result = min_max_sum(lst_nums)
print(result)


""" ____________ Min Max and Sum _____________


Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print the min and max values of the given numbers and the sum of all the numbers in the list.

Use min(), max() and sum().

The output should be as follows:
    •	On the first line: "The minimum number is {minimum number}"
    •	On the second line: "The maximum number is {maximum number}"
    •	On the third line: "The sum number is: {sum of all numbers}"


__________ Test Data ___________


Input 1:
-------
2 4 6


Output 1:
--------
The minimum number is 2
The maximum number is 6
The sum number is: 12


--------------------------------


Input 2:
-------
12 52 11 53 2 8 45


Output 2:
--------
The minimum number is 2
The maximum number is 53
The sum number is: 183


-------------------------------
"""
