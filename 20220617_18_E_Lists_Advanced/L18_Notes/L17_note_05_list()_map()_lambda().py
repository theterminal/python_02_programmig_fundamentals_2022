# 20220617 - Python - Lists Advance - Lecture
# Note - 05 - list(), map(), lambda()


powers_2 = list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))
print(powers_2)                                                         # [2, 4, 6, 8, 10]


# -----------------------------------------------------


powers_2 = list(map(lambda x: x * 2, list(range(5))))
print(powers_2)                                                         # [0, 2, 4, 6, 8]


# -----------------------------------------------------


def power_n(x):
    return x ** 2


print(list(map(power_n, [1, 2, 3, 4, 5])))                              # [1, 4, 9, 16, 25]
