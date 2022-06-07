# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 02 - Largest of Three Numbers - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#1

# ------------------ version 2 ------------------------

num_1, num_2, num_3 = int(input()), int(input()), int(input())

if num_1 > num_2 and num_1 > num_3:
    print(num_1)
elif num_2 > num_1 and num_2 > num_3:
    print(num_2)
else:
    print(num_3)
