# 20220529 - Python - Python Fundamentals - L08 - Data Types and Variables
# 01 - Concat Names - judge url: https://judge.softuni.org/Contests/Practice/Index/1721#0


# ------------- version 1 ----------------------- judge: 100%


name_1 = input()
name_2 = input()
delimiter = input()

print(f'{name_1}{delimiter}{name_2}')


"""---------------- Concat Names --------------------


Write a program that reads two names and a delimiter.
It should print the names joined by the delimiter.


------------ Test Data -----------------


Input 1:
-------
John
Smith
->


Output 1:
--------
John->Smith


----------------------------------------


Input 2:
-------
Jan
White
<->


Output 2:
--------
Jan<->White


----------------------------------------


Input 3:
-------
Linda
Terry
=>


Output 3:
--------
Linda=>Terry


"""
