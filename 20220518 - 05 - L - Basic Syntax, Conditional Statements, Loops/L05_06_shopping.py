# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 06 - Shopping - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#5


# ----------- version 1 -------------------------------- judge: 100%


budget = int(input())

while True:
    price_entered = input()
    if price_entered == 'End':
        print('You bought everything needed.')
        break

    budget -= int(price_entered)
    if budget < 0:
        print('You went in overdraft!')
        break


""" ------------------- Shopping --------------------


Write a program that reads an integer number representing a budget.
On the following lines, it reads integer numbers representing the prices of each product you should buy until it receives the command "End".
During the iterations, if there is not enough budget left to buy the next product, it prints "You went in overdraft!" and end the program.
Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."


---------- Test Data ----------


Input 1:
-------
100
5
End


Output 1:
--------
You bought everything needed.


--------------------------------


Input 2:
-------
50
25
20
10


Output 2:
--------
You went in overdraft!

"""