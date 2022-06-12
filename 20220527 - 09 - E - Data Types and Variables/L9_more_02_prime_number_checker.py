# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# More Exercises 02 - Prime Number Checker - judge url: https://judge.softuni.org/Contests/Practice/Index/1723#1

num = int(input())

if num <= 1:
    print('False')
else:
    for i in range(2, num):
        if num % i == 0:
            print('False')
            break
    else:
        print('True')
