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
