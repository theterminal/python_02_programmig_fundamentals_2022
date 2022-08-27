# 22020624 - Python - L12 - Lists Basics - More Exercise
# 05 - Tic Tac Toe - judge url: https://judge.softuni.org/Contests/Practice/Index/1726#4


# _________________ version 1 ___________________ judge 100%


line_1 = list(map(int, input().split(' ')))
line_2 = list(map(int, input().split(' ')))
line_3 = list(map(int, input().split(' ')))

winner = ''

if line_1[0] == line_1[1] == line_1[2] == 1:
    winner = 1
elif line_1[0] == line_1[1] == line_1[2] == 2:
    winner = 2

elif line_2[0] == line_2[1] == line_2[2] == 1:
    winner = 1
elif line_2[0] == line_2[1] == line_2[2] == 2:
    winner = 2

elif line_3[0] == line_3[1] == line_3[2] == 1:
    winner = 1
elif line_3[0] == line_3[1] == line_3[2] == 2:
    winner = 2

elif line_1[0] == line_2[0] == line_3[0] == 1:
    winner = 1
elif line_1[0] == line_2[0] == line_3[0] == 2:
    winner = 2

elif line_1[1] == line_2[1] == line_3[1] == 1:
    winner = 1
elif line_1[1] == line_2[1] == line_3[1] == 2:
    winner = 2

elif line_1[2] == line_2[2] == line_3[2] == 1:
    winner = 1
elif line_1[2] == line_2[2] == line_3[2] == 2:
    winner = 2

elif line_1[0] == line_2[1] == line_3[2] == 1:
    winner = 1
elif line_1[0] == line_2[1] == line_3[2] == 2:
    winner = 2

elif line_1[2] == line_2[1] == line_3[0] == 1:
    winner = 1
elif line_1[2] == line_2[1] == line_3[0] == 2:
    winner = 2


if winner == 1:
    print('First player won')
elif winner == 2:
    print('Second player won')
else:
    print('Draw!')


""" _______________ Tic Tac Toe ____________________


You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.

Legend:
•	0 - empty space
•	1 - first player move
•	2 - second player move

Find out who the winner is.
If the first player wins, print "First player won".
If the second player wins, print "Second player won".
Otherwise, print "Draw!".


____________ Test Data _______________


Input 1:
-------
2 0 1
0 1 0
1 0 2


Output 1:
--------
First player won


--------------------------------------


Input 2:
-------
0 1 0
2 2 2
1 0 0


Output 2:
--------
Second player won


-------------------------------------


Input 3:
-------
1 0 2
0 1 2
1 2 0


Output 3:
--------
Draw!


-------------------------------------
"""
