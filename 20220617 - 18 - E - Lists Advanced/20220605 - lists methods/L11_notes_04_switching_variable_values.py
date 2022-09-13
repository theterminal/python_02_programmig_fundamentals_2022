# 20220601 - Python - L11 - Lists Basics
# Notes 04


# ------------------------ Switching variable values --------
print('\n----- ex. 1 ----- Switching variable values -----\n')

a = 5
b = 10
print(f'a = {a}; b = {b}')

a, b = b, a
print(f'a = {a}; b = {b}')


# ------------------------ Switching elements in a list - short way --------
print('\n----- ex. 2 ----- Switching elements in a list - short way -----\n')

lst_20 = ['a', 'b', 'c']
print(lst_20)

lst_20[0], lst_20[-1] = lst_20[-1], lst_20[0]
print(lst_20)

