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


""" -------------------- Balanced Brackets --------------------


On the first line, you will receive 'n' – the number of lines, which will follow.
On the following 'n' lines, you will receive one of the following:

    •	Opening bracket – "(",
    •	Closing bracket – ")" or
    •	Random string

Your task is to find out if the brackets are balanced.
That means after every closing bracket should follow an opening one.
Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist,
the expression should be marked as unbalanced.

You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.


---------- Test Data -----------


Input 1:
-------
8
(
5 + 10
)
* 2 +
(
5
)
-12


Output 1:
--------
BALANCED


-------------------------------


Input 2:
-------
6
12 *
)
10 + 2 -
( 
5 + 10
)


Output 2:
--------
UNBALANCED


------------------------------

"""
