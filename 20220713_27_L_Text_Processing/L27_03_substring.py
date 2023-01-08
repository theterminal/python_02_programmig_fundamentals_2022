# 20220714 - Python - String Processing - Lecture
# 03 - Substring - judge url: https://judge.softuni.org/Contests/Practice/Index/1739#2


# ------------------------- version 1 -------------- judge: 100%


first: str = input()
second: str = input()

while first in second:
    second = second.replace(first, '')

print(second)
