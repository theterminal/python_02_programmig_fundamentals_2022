# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# More Exercises 01 - Exchange Integers - judge url: https://judge.softuni.org/Contests/Practice/Index/1723#0


# ---------------- version 2 ------------------ judge 100%


num_1, num_2 = int(input()), int(input())

print(f'Before:\na = {num_1}\nb = {num_2}')

num_temp = num_1
num_1 = num_2
num_2 = num_temp

print(f'After:\na = {num_1}\nb = {num_2}')


# ---------------- version 1 ------------------ judge gives 100% but logically is NOT correct


num_1, num_2 = int(input()), int(input())

print(f'Before:\na = {num_1}\nb = {num_2}')
print(f'After:\na = {num_2}\nb = {num_1}')


""" ------------------- Exchange Integers ----------------------


Read two integer numbers and, after that, exchange their values.
Print the variable values before and after the exchange, as shown below:


-------- Test Data ---------


Input 1:
-------
5
10


Output 1:
--------
Before:
a = 5
b = 10
After:
a = 10
b = 5


----------------------------


Input 2:
-------
10
20


Output 2:
--------
Before:
a = 10
b = 20
After:
a = 20
b = 10


---------------------------

"""
