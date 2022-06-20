# 20220615 - Python Code - Functions - More Exercise
# 02 - Center Point - judge url: https://judge.softuni.org/Contests/Practice/Index/1729#1


import math


def center_point(x1, y1, x2, y2):

    if (abs(x1) + abs(y1)) == (abs(x2) + abs(y2)):
        return f'({math.floor(x1)}, {math.floor(y1)})'

    elif (abs(x1) + abs(y1)) < (abs(x2) + abs(y2)):
        return f'({math.floor(x1)}, {math.floor(y1)})'

    else:
        return f'({math.floor(x2)}, {math.floor(y2)})'


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

result = center_point(x_1, y_1, x_2, y_2)
print(result)
