# 20220617 - Python Code - Lists Advance - Lecture
# Notes - 05 - map()


powers_2 = list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))
print(powers_2)


# -----------------------------------------------------


powers_2 = list(map(lambda x: x * 2, list(range(5))))
print(powers_2)


# -----------------------------------------------------


def power_n(x):
    return x ** 2


print(list(map(power_n, [1, 2, 3, 4, 5])))


