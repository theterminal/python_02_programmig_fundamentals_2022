# 20220614 - Python Code - Functions - Exercise
# 02 - Add and Subtract - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#1

# ------------------ version 3 ------------------


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


# ------------------ version 2 ------------------


def sum_numbers(z1, z2):
    return z1 + z2


def subtract(sum_z1_z2, z3):
    return sum_z1_z2 - z3


def add_and_subtract(z1, z2, z3):
    sum_z1_z2 = sum_numbers(z1, z2)
    result = subtract(sum_z1_z2, z3)
    return result


z_1 = int(input())
z_2 = int(input())
z_3 = int(input())

print(add_and_subtract(z_1, z_2, z_3))


# ------------------ version 1 ------------------


def sum_numbers(x1, x2):
    return x1 + x2


def subtract(sum_x1_plus_x2, x3):
    return sum_x1_plus_x2 - x3


def add_and_subtract(z1, z2, z3):
    sum_of_1_and_2 = sum_numbers(z1, z2)
    result = subtract(sum_of_1_and_2, z3)
    return result


a_a = int(input())
b_b = int(input())
c_c = int(input())

print(add_and_subtract(a_a, b_b, c_c))
