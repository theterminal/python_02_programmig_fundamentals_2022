# 20220713 - Python Code - Dictionaries - Exercise
# 02 - A Miner Task - judge url: https://judge.softuni.org/Contests/Compete/Index/1737#1


# ------------- version 1 ------------------- judge: 100%


dct = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())

    if resource not in dct.keys():
        dct[resource] = 0
    dct[resource] += quantity

for k, v in dct.items():
    print(f'{k} -> {v}')
