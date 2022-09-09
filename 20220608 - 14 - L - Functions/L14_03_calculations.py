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


""" _______________ Calculations ________________


Create a function that receives three parameters, calculates a result depending on the given operator, and returns it.
Print the result of the function.

The input comes as three parameters – an operator as a string and two integer numbers.
The operator can be one of the following: 
"multiply", "divide", "add", "subtract". 


____________ Test Data _____________


Input 1:
-------
subtract
5
4


Output 1:
--------
1


------------------------------------


Input 2:
-------
divide
8
4


Output 2:
--------
2


-----------------------------------
"""
