# 20220614 - Python - Functions - Lecture
# 07 - Rounding - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#6


# -------------- version 1 --------------------- judge 100%


def rounding(lst: list):
    lst_num = [round(float(i)) for i in lst_in]

    return lst_num


lst_in = input().split(' ')
print(rounding(lst_in))


# -------------- version 2 --------------------- judge 100%


print(list(map(lambda a: round(float(a)), input().split(' '))))


""" ____________ Rounding _____________


Input 1:
-------
1.0 2.5 3.0 4.5


Output 1:
--------
[1, 2, 3, 4]


---------------------------------------


Input 2:
-------
2.56 1.9 -3.4 8.1


Output 2:
--------
[3, 2, -3, 8]


---------------------------------------
"""
