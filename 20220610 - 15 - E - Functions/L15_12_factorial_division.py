# 20220615 - Python Code - Functions - Exercise
# 12 - Factorial Division - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#11


# -------------- version 2 --------------------------


def factorial_calculation(num):
    for i in range(1, num):
        num *= i
    return num


num_int_1 = int(input())
num_int_2 = int(input())

num_1_factorial = factorial_calculation(num_int_1)
num_2_factorial = factorial_calculation(num_int_2)
result = num_1_factorial / num_2_factorial

print(f'{result:.2f}')


# -------------- version 1 --------------------------


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
