# 20220614 - Python - Functions - Exercise
# 02 - Add and Subtract - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#1


# ------------------ version 3 ------------------ judge 100%


def sum_numbers(z1, z2):
    return z1 + z2


def subtract(sum_z1_z2, z3):
    return sum_z1_z2 - z3


def add_and_subtract(z1, z2, z3):
    return subtract(sum_numbers(z1, z2), z3)


z_1 = int(input())
z_2 = int(input())
z_3 = int(input())

print(add_and_subtract(z_1, z_2, z_3))


# ------------------ version 2 ------------------ judge 100%


def sum_nums(z1, z2):
    return z1 + z2


def subtract_2(sum_z1_z2, z3):
    return sum_z1_z2 - z3


def add_and_subtract(z1, z2, z3):
    sum_z1_z2 = sum_nums(z1, z2)
    return subtract_2(sum_z1_z2, z3)


z_1 = int(input())
z_2 = int(input())
z_3 = int(input())

print(add_and_subtract(z_1, z_2, z_3))


# ------------------ version 1 ------------------ judge 100%


def sum_nums_2(x1, x2):
    return x1 + x2


def subtract_3(sum_x1_plus_x2, x3):
    return sum_x1_plus_x2 - x3


def add_and_subtract(z1, z2, z3):
    sum_of_1_and_2 = sum_nums_2(z1, z2)
    result = subtract_3(sum_of_1_and_2, z3)
    return result


a_a = int(input())
b_b = int(input())
c_c = int(input())

print(add_and_subtract(a_a, b_b, c_c))


""" _______________ Add & Subtract _______________


You will receive three integer numbers.

Write functions named:
•	'sum_numbers()' that returns the sum of the first two integers
•	'subtract()' that returns the difference between the returned result of the first function and the third integer

Wrap the two functions in a function named 'add_and_subtract()' which will receive the three numbers as parameters.
Print the result of the subtract() function on the console.


___________ Test Data ____________


Input 1:
-------
23
6
10


Output 1:
--------
19


----------------------------------


Input 2:
-------
1
17
30


Output 2:
--------
-12


----------------------------------


Input 3:
-------
42
58
100


Output 3:
--------
0


----------------------------------
"""
