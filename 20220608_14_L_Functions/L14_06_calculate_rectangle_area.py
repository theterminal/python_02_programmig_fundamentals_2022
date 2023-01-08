# 20220614 - Python - Functions - Lecture
# 06 - Calculate Rectangle Area - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#5


# -------------- version 1 --------------------- judge 100%


def rectangle_area(width: int, height: int):
    return width * height


w = int(input())
h = int(input())

print(rectangle_area(w, h))
