# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 07 - Patterns - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#6


# ------------- version 2 ----------------------- judge: 100%


num_stars_max_per_row = int(input())

for num_stars_to_print in range(1, num_stars_max_per_row + 1):
    for j in range(0, num_stars_to_print):
        print('*', end="")
    print()

for num_stars_to_print in range(num_stars_max_per_row - 1, 0, -1):
    for j in range(0, num_stars_to_print):
        print('*', end="")
    print()


# ------------ version 1 ----------------------- judge: 100%


num_stars_max_per_row = int(input())

# prints out top half of the figure
for num_stars_to_print in range(1, num_stars_max_per_row + 1):
    print(num_stars_to_print * '*')

# prints out the second half of the figure
for num_stars_to_print in range(num_stars_max_per_row - 1, 0, -1):
    print(num_stars_to_print * '*')


""" ----------------------------- Patterns --------------------------------


Write a program that receives a number and creates the following pattern.
The number represents the largest count of stars on one row.


------------------ Test Data ------------------


Input 1:
-------
3


Output 1:
--------
*
**
***
**
*


------------------------------------------------


Input 2:
-------
5


Output 2:
--------
*
**
***
****
*****
****
***
**
*


"""