# 20220614 - Python - Functions - Lecture
# 06 - Calculate Rectangle Area - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#5


def rectangle_area(width: int, height: int):
    return width * height


w = int(input())
h = int(input())

print(rectangle_area(w, h))


""" __________________ Calculating Rectangle Area ______________________


Create a function that calculates and returns the area of a rectangle by given width and height.
Print the result on the console.


____________ Test Data ______________


Input 1:
-------
3
4


Output 1:
--------
12


-------------------------------------


Input 2:
-------
6
2


Output 2:
--------
12


------------------------------------
"""
