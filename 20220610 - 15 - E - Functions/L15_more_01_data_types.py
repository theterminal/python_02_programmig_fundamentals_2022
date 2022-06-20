# 20220615 - Python Code - Functions - More Exercise
# 01 - Data Types - judge url: https://judge.softuni.org/Contests/Practice/Index/1729#0


def data_types(type_1, value_1):
    if type_1 == 'int':
        return int(value_1) * 2
    elif type_1 == 'real':
        return f'{(float(value_1) * 1.5):.2f}'
    elif type_1 == 'string':
        return f'${value_1}$'


type_in = input()
value_in = input()

print(data_types(type_in, value_in))
