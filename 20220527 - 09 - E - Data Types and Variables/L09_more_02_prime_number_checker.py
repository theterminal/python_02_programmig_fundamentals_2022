# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# More Exercises 02 - Prime Number Checker - judge url: https://judge.softuni.org/Contests/Practice/Index/1723#1


# --------- version 1 --------------------- judge 100%


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


""" --------------- Prime Number Checker -------------------


Write a program to check if a number is prime.
A prime number is a natural number greater than 1, not a product of two smaller natural numbers.
For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.

The input comes as an integer number.
The output should be 'True' if the number is prime and 'False' otherwise.


----------- Test Data ------------


Input 1:
-------
7


Output 1:
--------
True


----------------------------------


Input 2:
-------
8


Output 2:
--------
False


----------------------------------


Input 3:
-------
81


Output 3:
--------
False


---------------------------------

"""
