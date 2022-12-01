# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# More Exercises 04 - Balanced Brackets - judge url: https://judge.softuni.org/Contests/Practice/Index/1723#3


# --------- version 1 --------------------- judge 100%


num_lines = int(input())
counter = 0
flag = False

for _ in range(num_lines):
    char = input()

    if char == '(':
        counter += 1

        if counter > 1:
            flag = True
            break

    if char == ')':
        if counter != 1:
            flag = True
            break
        else:
            counter = 0

if flag:
    print('UNBALANCED')
else:
    print('BALANCED')
