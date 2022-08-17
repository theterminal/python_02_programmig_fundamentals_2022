# 20220614 - Python Code - Functions - Exercise
# 05 - Even Numbers - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#4


# ----------------------- version 5 using lambda -------------- judge 100%


print(list(filter(lambda x: x % 2 == 0, [int(i) for i in input().split()])))


# ----------------------- version 4 using lambda -------------- judge 100%


numbers = [int(i) for i in input().split()]
print(list(filter(lambda x: x % 2 == 0, numbers)))


# ----------------------- version 3 --------------------------- judge 100%


numbers = [int(i) for i in input().split() if int(i) % 2 == 0]
print(numbers)


# ----------------------- version 2 --------------------------- judge 100%


def check_numbers(num):
    if num % 2 == 0:
        result = True
    else:
        result = False

    return result


numbers = [int(i) for i in input().split()]
print(list(filter(check_numbers, numbers)))


# ----------------------- version 1 --------------------------- judge 100%


def check_numbers(num):
    if num % 2 == 0:
        result = True
    else:
        result = False

    return result


str_num_in = input().split()
numbers = [int(i) for i in str_num_in]
print(list(filter(check_numbers, numbers)))


""" ____________ Even Numbers ____________


Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print a list of only the even numbers.
Use 'filter()'.


___________ Test Data ____________


Input 1:
-------
1 2 3 4


Output 1:
--------
[2, 4]


----------------------------------


Input 2:
-------
1 2 3 -1 -2 -3


Output 2:
--------
[2, -2]


----------------------------------
"""
