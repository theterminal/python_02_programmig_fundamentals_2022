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


''' ------------- String Pureness ----------------


You will be given number 'n'.
After that, you'll receive different strings 'n' times.

Your task is to check if the given strings are pure, meaning that they do NOT consist of any of the characters:

    comma ","
    period "."
    underscore "_"
    
    •	If a string is pure, print "{string} is pure."
    •	Otherwise, print "{string} is not pure!"


--------- Test Data ----------


Input 1:
-------
2
pure string
not_pure_string


Output 1:
--------
pure string is pure.
not_pure_string is not pure!


------------------------------


Input 2:
-------
3
SoftUni
12345
string.pureness


Output 2:
--------
SoftUni is pure.
12345 is pure.
string.pureness is not pure!


'''
