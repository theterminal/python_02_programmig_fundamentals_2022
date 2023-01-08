# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 06 - Shopping - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#5


# ----------- version 1 -------------------------------- judge: 100%


budget = int(input())

while True:
    price_entered = input()
    if price_entered == 'End':
        print('You bought everything needed.')
        break

    budget -= int(price_entered)
    if budget < 0:
        print('You went in overdraft!')
        break
