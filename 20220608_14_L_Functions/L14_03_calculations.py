# 20220614 - Python - Functions - Lecture
# 03 - Calculations - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#2


# ------- using normal function --------- judge 100%


def calculations(operator_1, int_1, int_2):
    result = None

    if operator_1 == 'multiply':
        result = int_1 * int_2

    elif operator_1 == 'divide':
        result = int(int_1 / int_2)

    elif operator_1 == 'add':
        result = int_1 + int_2

    elif operator_1 == 'subtract':
        result = int_1 - int_2

    return result


in_1 = input()
in_2 = int(input())
in_3 = int(input())

print(calculations(in_1, in_2, in_3))


# ------- using import operator module -------- judge 100%


import operator


def repeat_string_2(operation, num_1, num_2):
    op_dict = {'add': operator.add, 'subtract': operator.sub,
               'multiply': operator.mul, 'divide': operator.truediv}

    return int(op_dict[operation](num_1, num_2))


in_1 = input()
in_2 = int(input())
in_3 = int(input())

print(repeat_string_2(in_1, in_2, in_3))
