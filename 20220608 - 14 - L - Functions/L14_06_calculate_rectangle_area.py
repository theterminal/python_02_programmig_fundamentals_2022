# 20220614 - Python Code - Functions - Lecture
# 06 - Calculate Rectangle Area - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#5


def rectangle_area(width: int, height: int):
    result = width * height
    return result


w = int(input())
h = int(input())
print(rectangle_area(w, h))
