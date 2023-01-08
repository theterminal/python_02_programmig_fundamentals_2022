# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 05 - Number Between 1 and 100 - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#4


# ----------- version 2 -------------------------------- judge: 100%


num = float(input())

while not (1 <= num <= 100):
    num = float(input())

print(f'The number {num} is between 1 and 100')


# ----------- version 1 -------------------------------- judge: 100%


while True:
    num = float(input())
    if 1 <= num <= 100:
        print(f'The number {num} is between 1 and 100')
        break
