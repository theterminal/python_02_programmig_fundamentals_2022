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


""" ------------- Even Numbers ---------------


Write a program that receives a number n on the first line.
On the following n lines, it receives different integer numbers.
If the program receives an odd number, print "{num} is odd!" and end the program. 
Otherwise, if all numbers given are even, print "All numbers are even.".


Input 1:
-------
2
12
286


Output 1:
--------
All numbers are even.


-----------------------------------------------


Input 2:
-------
5
2
9


Output 2:
--------
9 is odd!


"""
