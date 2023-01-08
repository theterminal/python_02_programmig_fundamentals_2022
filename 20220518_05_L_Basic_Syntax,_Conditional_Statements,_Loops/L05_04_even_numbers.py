# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 04 - Even Numbers - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#3


# --------------------- version 1 --------------------------- judge: 100%


n = int(input())

for i in range(n):
    num = int(input())
    if num % 2 != 0:
        print(f'{num} is odd!')
        break
else:
    print('All numbers are even.')
