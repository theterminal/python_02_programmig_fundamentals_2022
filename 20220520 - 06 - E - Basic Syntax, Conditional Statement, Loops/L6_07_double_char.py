# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 07 - Double Char - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#6

while True:
    str_to_test = input()
    if str_to_test == "End":
        break
    if str_to_test == "SoftUni":
        continue

    for j, k in enumerate(str_to_test):
        print(k * 2, end="")
    print()
