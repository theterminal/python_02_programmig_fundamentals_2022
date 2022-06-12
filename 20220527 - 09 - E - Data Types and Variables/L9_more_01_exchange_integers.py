# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# More Exercises 01 - Exchange Integers - judge url: https://judge.softuni.org/Contests/Practice/Index/1723#0

# ---------------- version 2 ------------------

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
