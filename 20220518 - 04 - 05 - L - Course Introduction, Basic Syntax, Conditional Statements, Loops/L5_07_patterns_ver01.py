# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 07 - Patterns - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#6


# ------------ version 1 -----------------------


num_stars_max_per_row = int(input())

# prints out top half of the figure
for num_stars_to_print in range(1, num_stars_max_per_row + 1):
    print(num_stars_to_print * '*')

# prints out the second half of the figure
for num_stars_to_print in range(num_stars_max_per_row - 1, 0, -1):
    print(num_stars_to_print * '*')
