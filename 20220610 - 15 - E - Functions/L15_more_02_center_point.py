# 20220615 - Python Code - Functions - More Exercise
# 02 - Center Point - judge url: https://judge.softuni.org/Contests/Practice/Index/1729#1

import math


# -------------- version 1 -------------------------- judge 100%


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


""" _____________ Center Point ______________


You will be given the coordinates of two points on a Cartesian coordinate system – (X1, Y1) and  (X2, Y2) on separate lines.

Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"
If the points are at the same distance from the center, print only the first one.
The resulting coordinates must be formatted to the lower integer.


_________ Test Data __________


Input 1:
-------
2
4
-1
2


Output 1:
--------
(-1, 2)


------------------------------


Input 2:
-------
10
14.5
-17.2
16


Output 2:
--------
(10, 14)


------------------------------
"""
