# 20220617 - Python - Lists Advance - Exercise
# 04 - Number Classification - judge: https://judge.softuni.org/Contests/Compete/Index/1731#3


# ------------------------ version 1 ---------------------------------- judge 100%


lst_int_input = list(map(int, input().split(', ')))

print(f'Positive: {", ".join([str(i) for i in lst_int_input if i >= 0])}')
print(f'Negative: {", ".join([str(i) for i in lst_int_input if i < 0])}')
print(f'Even: {", ".join([str(i) for i in lst_int_input if i % 2 == 0])}')
print(f'Odd: {", ".join([str(i) for i in lst_int_input if i % 2 == 1])}')


# ------------------------- version 2 --------------------------------- judge 100%


def positive_numbers(lst_nums):
    return [str(i) for i in lst_nums if i >= 0]


def negative_numbers(lst_nums):
    return [str(i) for i in lst_nums if i < 0]


def even_numbers(lst_nums):
    return [str(i) for i in lst_nums if i % 2 == 0]


def odd_numbers(lst_nums):
    return [str(i) for i in lst_nums if i % 2 == 1]


lst_int_in = list(map(int, input().split(', ')))

print(f'Positive: {", ".join(positive_numbers(lst_int_in))}')
print(f'Negative: {", ".join(negative_numbers(lst_int_in))}')
print(f'Even: {", ".join(even_numbers(lst_int_in))}')
print(f'Odd: {", ".join(odd_numbers(lst_int_in))}')


""" ______________ Number Clssification ________________


Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
and prints all the positive, negative, even, and odd numbers on separate lines as shown below.

Note: Zero is counted for a positive number


________ Test Data ___________


Input 1:
-------
1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33


Output 1:
--------
Positive: 1, 0, 5, 3, 4, 12, 19
Negative: -2, -100, -20, -33
Even: -2, 0, 4, -100, -20, 12
Odd: 1, 5, 3, 19, -33


------------------------------


Input 2:
-------
1, 2, 53, 2, 21


Output 2:
--------
Positive: 1, 2, 53, 2, 21
Negative:
Even: 2, 2
Odd: 1, 53, 21


------------------------------
"""
