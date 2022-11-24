# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 06 - String Pureness - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#5


# ----------------- version 4 -------------------- judge: 100%


num_n = int(input())
lst_to_test = [',', '.', '_']

for _ in range(num_n):
    str_to_test = input()

    for i in range(len(lst_to_test)):
        if lst_to_test[i] in str_to_test:
            print(f'{str_to_test} is not pure!')
            break
    else:
        print(f'{str_to_test} is pure.')


# ----------------- version 3 -------------------- judge: 100%


num_n = int(input())

for _ in range(num_n):
    str_to_test = input()

    if ',' in str_to_test or '.' in str_to_test or '_' in str_to_test:
        print(f'{str_to_test} is not pure!')
    else:
        print(f'{str_to_test} is pure.')


# ----------------- version 2 -------------------- judge: 100%


num_n = int(input())

for i in range(num_n):
    str_to_test = input()
    for k, j in enumerate(str_to_test):
        if j == ',' or j == '.' or j == '_':
            print(f'{str_to_test} is not pure!')
            break
    else:
        print(f'{str_to_test} is pure.')


# ------------------ version 1 ------------------- judge: 100%


num_n = int(input())
flag = False

for i in range(num_n):
    str_to_test = input()
    for k, j in enumerate(str_to_test):
        if j == ',' or j == '.' or j == '_':
            flag = True
    if flag:
        print(f'{str_to_test} is not pure!')
    else:
        print(f'{str_to_test} is pure.')

    flag = False
