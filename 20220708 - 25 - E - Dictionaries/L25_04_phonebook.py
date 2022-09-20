# 20220713 - Python - Dictionaries - Exercise
# 04 - Phonebook - judge url: https://judge.softuni.org/Contests/Compete/Index/1737#3


# ------------- version 1 -------------------- judge: 100%


dct = {}

while True:
    data = input()
    if data.isdigit():
        data = int(data)
        break

    name, number = data.split('-')

    dct[name] = number

for i in range(data):
    person = input()
    if person in dct.keys():
        print(f'{person} -> {dct[person]}')
    else:
        print(f'Contact {person} does not exist.')
