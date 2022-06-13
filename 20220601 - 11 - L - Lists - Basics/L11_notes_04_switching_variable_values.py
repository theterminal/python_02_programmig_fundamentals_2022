# 20220601 - Python Code - L11 - Lists Basics
# Notes 03 - Switching Variables Names

# # -------------- switching variable values ---------------------
print('\nSwitching variable values')

a = 5
b = 10
print(f'a = {a}; b = {b}')

a, b = b, a
print(f'a = {a}; b = {b}')


# -------------- switching elements in a list - short way ---------
print('\nSwitching elements in a list - short way')

lst_1 = ['a', 'b', 'c']
print(lst_1)

lst_1[0], lst_1[-1] = lst_1[-1], lst_1[0]
print(lst_1)

