# 20220617 - Python Code - Lists Advance - Exercise
# 04 - Number Classification - judge: https://judge.softuni.org/Contests/Compete/Index/1731#3


# ------------------------ version 1 ----------------------------------


lst_int_input = list(map(int, input().split(', ')))

print(f'Positive: {", ".join([str(i) for i in lst_int_input if i >= 0])}')
print(f'Negative: {", ".join([str(i) for i in lst_int_input if i < 0])}')
print(f'Even: {", ".join([str(i) for i in lst_int_input if i % 2 == 0])}')
print(f'Odd: {", ".join([str(i) for i in lst_int_input if i % 2 == 1])}')


# ------------------------- version 2 ---------------------------------


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
