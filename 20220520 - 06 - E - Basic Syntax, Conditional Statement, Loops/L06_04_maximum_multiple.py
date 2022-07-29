# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 04 - Maximum Multiple - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#3


# ------------- version 1 ----------------------- judge: 100%


divisor = int(input())
boundary = int(input())
max_multiplier = 0

for current_num in range(boundary, divisor, -1):
    if current_num % divisor == 0:
        max_multiplier = current_num
        print(max_multiplier)
        break


# ------------- version 2 ----------------------- judge: 100% --- (from Юри Димитров)


divisor = int(input())
boundary = int(input())

print((boundary // divisor) * divisor)


""" ------------------- Maximum Multiple ----------------------


On the first line, you will be given a positive number, which will serve as a divisor. 
On the second line, you will receive a positive number that will be the boundary.

You should find the largest integer N, that is:

•	divisible by the given divisor
•	less than or equal to the given bound
•	greater than 0

Note: it is guaranteed that N is found.


---------- Test Data ----------------


Input 1:
-------
2
7


Output 1:
--------
6


-------------------------------------


Input 2:
-------
10
50


Output 2:
--------
50


-------------------------------------


Input 3:
-------
37
200


Output 3:
--------
185


"""
