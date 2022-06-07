# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 01 - Number Definer - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#0

num_entered = float(input())

if num_entered == 0:
    print('zero')
elif num_entered > 0:
    if num_entered < 1:
        print('small positive')
    elif num_entered > 100000:
        print('large positive')
    else:
        print('positive')
else:
    if num_entered > -1:
        print('small negative')
    elif num_entered < -1000000:
        print('large negative')
    else:
        print('negative')
