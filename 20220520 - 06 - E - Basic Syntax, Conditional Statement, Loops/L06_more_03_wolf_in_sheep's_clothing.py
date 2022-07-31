# 20220528 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# More Exercise 03 - Wolf in Sheep's Clothing - judge url: https://judge.softuni.org/Contests/Practice/Index/1720#2


# ------------------------ version 1 ------------------------------------------- judge: 100%


lst_1 = input().split(', ')
index_wolf = ''

for i in range(len(lst_1)):
    if lst_1[i] == 'wolf':
        index_wolf = i

if index_wolf == (len(lst_1) - 1):
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {len(lst_1) - index_wolf - 1}! You are about to be eaten by a wolf!')


""" ------------------- Wolf in Sheep's Clothing -----------------------


Wolves have been reintroduced to Great Britain.
You are a sheep farmer and are now plagued by wolves who pretend to be sheep.
Fortunately, you are good at spotting them.

Warn the sheep in front of the wolf that it is about to be eaten.
Remember that you are standing at the front of the queue, which is at the end of the list:

[sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   4      3            2      1

If the wolf is the closest animal to you, print:
"Please go away and stop eating my sheep".

Otherwise, return:
"Oi! Sheep number N! You are about to be eaten by a wolf!"
where 'N' is the sheep's position in the queue.

Note: there will always be exactly one wolf on the list.


"Input"
-------
The input will be a single string containing the animals separated by a comma and a single space ", "


---------------- Test Data -------------------


Input 1:
-------
sheep, sheep, wolf


Output 1:
--------
Please go away and stop eating my sheep


----------------------------------------------


Input 2:
-------
wolf, sheep, sheep, sheep, sheep, sheep


Output 2:
--------
Oi! Sheep number 5! You are about to be eaten by a wolf!


"""
