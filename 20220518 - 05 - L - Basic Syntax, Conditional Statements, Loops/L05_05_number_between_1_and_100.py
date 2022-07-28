# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 05 - Number Between 1 and 100 - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#4


# ----------- version 2 -------------------------------- judge: 100%


num = float(input())

while not (1 <= num <= 100):
    num = float(input())

print(f'The number {num} is between 1 and 100')


# ----------- version 1 -------------------------------- judge: 100%


while True:
    num = float(input())
    if 1 <= num <= 100:
        print(f'The number {num} is between 1 and 100')
        break


""" --------------- Number Between 1 and 100 ----------------


Write a program that reads different floating-point numbers from the console.
When it receives a number between 1 and 100 inclusive, the program should stop reading and should print "The number {number} is between 1 and 100".


------------------ Examples -------------------


Input 1:
-------
-3
0.9
44


Output 1:
--------
The number 44.0 is between 1 and 100


------------------------------------


Input 2:
-------
0.5
90
-4
101


Output 2:
--------
The number 90.0 is between 1 and 100


"""