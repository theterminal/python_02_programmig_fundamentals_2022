# 20220614 - Python Code - Functions - Lecture
# 03 - Calculations - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#2

# ------- using normal function --------


# def calculations(operator, int_1, int_2):
#
#     result = None
#
#     if operator == 'multiply':
#         result = int_1 * int_2
#
#     elif operator == 'divide':
#         result = int(int_1 / int_2)
#
#     elif operator == 'add':
#         result = int_1 + int_2
#
#     elif operator == 'subtract':
#         result = int_1 - int_2
#
#     return result
#
#
# in_1 = input()
# in_2 = int(input())
# in_3 = int(input())
# print(calculations(in_1, in_2, in_3))


# ------- using import operator module --------


import operator


def repeat_string_2(operation, num_1, num_2):
    op_dict = {'add': operator.add, 'subtract': operator.sub,
               'multiply': operator.mul, 'divide': operator.truediv}

    return int(op_dict[operation](num_1, num_2))


in_1 = input()
in_2 = int(input())
in_3 = int(input())
print(repeat_string_2(in_1, in_2, in_3))
