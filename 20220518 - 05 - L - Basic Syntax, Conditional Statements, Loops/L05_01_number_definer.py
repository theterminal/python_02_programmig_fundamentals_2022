# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 01 - Number Definer - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#0


# -------------------------------- version 1 ------------------------------------ judge: 100%


num_entered = float(input())

if num_entered == 0:
    print('zero')
elif num_entered > 0:
    if num_entered < 1:
        print('small positive')
    elif num_entered > 100000:
        print('large positive')
    else:
        print('positive')
else:
    if num_entered > -1:
        print('small negative')
    elif num_entered < -1000000:
        print('large negative')
    else:
        print('negative')


""" ------------------- Number Definer ----------------------


Write a program that reads a floating-point number and:

-	prints "zero" if the number is zero
-	prints "positive" or "negative"
-	adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds 1 000 000


--------------- Examples -----------------


Input 1:                Output 1:
-------                 --------
25                      positive


------------------------------------------


Input 2:                Output 2:
-------                 --------
0.7                     small positive


------------------------------------------


Input 3:                Output 3:
-------                 --------
435247392.921           large positive


------------------------------------------


Input 4:                Output 4:
-------                 --------
-0.005                  small negative


------------------------------------------


Input 5:                Output 5:
-------                 --------
-103.21                 negative


------------------------------------------


Input 6:                Output 6:
-------                 --------
-358583355123.001       large negative


"""