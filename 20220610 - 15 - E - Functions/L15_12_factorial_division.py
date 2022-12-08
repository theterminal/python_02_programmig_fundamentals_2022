# 20220615 - Python - Functions - Exercise
# 12 - Factorial Division - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#11


# -------------- version 3 -------------------------- judge 100%


def factorial_calculator(num):
    for i in range(1, num):
        num *= i
    return num


num_1 = int(input())
num_2 = int(input())

print(f'{(factorial_calculator(num_1) / factorial_calculator(num_2)):.2f}')


# -------------- version 2 -------------------------- judge 100%


def factorial_calculator(num):
    for i in range(1, num):
        num *= i
    return num


num_int_1 = int(input())
num_int_2 = int(input())

num_1_factorial = factorial_calculator(num_int_1)
num_2_factorial = factorial_calculator(num_int_2)
result = num_1_factorial / num_2_factorial

print(f'{result:.2f}')


# -------------- version 1 -------------------------- judge 100%


def division_of_factorials(num_1, num_2):

    factorial_num_1 = 1
    for i in range(1, num_1 + 1):
        factorial_num_1 *= i

    factorial_num_2 = 1
    for i in range(1, num_2 + 1):
        factorial_num_2 *= i

    return f'{(factorial_num_1 / factorial_num_2):.2f}'


num_int_1 = int(input())
num_int_2 = int(input())

print(division_of_factorials(num_int_1, num_int_2))
