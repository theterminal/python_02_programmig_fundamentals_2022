# 22020624 - Python Code - L12 - Lists Basics - More Exercise
# 05 - Tic Tac Toe - judge url: https://judge.softuni.org/Contests/Practice/Index/1726#4


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
