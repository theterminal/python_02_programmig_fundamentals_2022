# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 02 - Drink Something - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#1

persons_age_entered = int(input())

if persons_age_entered <= 14:
    print('drink toddy')
elif persons_age_entered <= 18:
    print('drink coke')
elif persons_age_entered <= 21:
    print('drink beer')
elif persons_age_entered > 21:
    print('drink whisky')
