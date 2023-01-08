# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# Notes 01


# -----------------------------------------------------------------


# Storing range into variable
a = range(1, 10)
for i in a:
    print(i, end=", ")


# -----------------------------------------------------------------


# this example shows that 'not' has the highest priority
if 2 > 1 or 3 < 4 and not 4 > 0:
    print('This will be printed')

# this example shows that 'and' is second in priority after 'not'
if (2 > 1 or 3 < 4) and not 4 > 0:
    print('This will NOT be printed')


# -----------------------------------------------------------------


# when iterable variable is not needed can use '_' only
for _ in range(45):
    print(65)


# -----------------------------------------------------------------
