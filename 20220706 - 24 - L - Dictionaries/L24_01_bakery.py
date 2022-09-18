# 20220706 - Python - Dictionaries - Lecture
# 01 - Bakery - judge url: https://judge.softuni.org/Contests/Practice/Index/1736#0


# --------------------- version 4 --------------------------- judge 100%


data = input().split(' ')
products = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}
print(products)


# --------------------- version 3 --------------------------- judge 100%


data = input().split(' ')
products = dict()

for i in range(0, len(data), 2):
    products[data[i]] = int(data[i + 1])

print(products)


# --------------------- version 2 --------------------------- judge 100%


items = input().split(' ')
inventory = {}

for i in range(len(items)):
    if i % 2 == 0:
        key = items[i]
        value = items[i + 1]
        inventory[key] = int(value)

print(inventory)


# --------------------- version 1 --------------------------- judge 100%


items = input().split(' ')
dictionary = dict()

for i in range(0, len(items), 2):
    key = items[i]
    value = items[i + 1]
    dictionary[key] = int(value)

print(dictionary)
