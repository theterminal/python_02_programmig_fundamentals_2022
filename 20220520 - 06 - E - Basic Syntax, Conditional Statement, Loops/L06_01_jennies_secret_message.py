# 20220520 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 01 - Jenny's Secret Message - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#0


# ------------- version 1 ----------------------- judge: 100%


name_entered = input()

if name_entered == 'Johnny':
    print(f'Hello, my love!')
else:
    print(f'Hello, {name_entered}!')


""" ------------------- Jenny's Secret Message ------------------


Jenny studies programming with Python and wants to create a program that greets the user when he/she gives his/her name.
The greeting should be in the format "Hello, {name}!".
However, Jenny is in love with Johnny and would like to greet him differently: "Hello, my love!".
Could you help her?


-------- Test Data --------------------


Input 1:                Output 1:
-------                 ---------
Peter                   Hello, Peter!


---------------------------------------


Input 2:                Output 2:
-------                 ---------
Amy                     Hello, Amy!


---------------------------------------


Input 3:                Output 3:
-------                 ---------
Johnny              	Hello, my love!


"""
