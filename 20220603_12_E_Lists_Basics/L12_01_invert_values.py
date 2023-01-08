# 20220603 - Python - L12 - Lists Basics - Exercise
# 01 - Invert Values - judge url: https://judge.softuni.org/Contests/Compete/Index/1725#0


# ---------------------- version 2 ----------------------- judge 100%


print(list(map(lambda x: int(x) * -1, input().split(' '))))


# ---------------------- version 1 ----------------------- judge 100%


list_start_values = input().split(' ')
list_opposite_values = list()

for element in list_start_values:
    list_opposite_values.append(-int(element))

print(list_opposite_values)
