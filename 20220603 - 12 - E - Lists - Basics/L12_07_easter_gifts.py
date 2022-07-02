# 22020603 - Python Code - L12 - Lists Basics - Exercise
# 07 - Easter Gifts - https://judge.softuni.org/Contests/Compete/Index/1725#6


# ______________ version 5 __________________100% judge


lst_gifts = list(map(str, input().split(' ')))

while True:
    command = input()
    if command == 'No Money':
        break

    command = command.split(' ')

    action = command[0]
    gift = command[1]

    if action == 'OutOfStock':
        while gift in lst_gifts:
            index_action = lst_gifts.index(gift)
            lst_gifts[index_action] = 'None'

    elif action == 'Required':
        if 0 <= int(command[2]) < len(lst_gifts):
            lst_gifts[int(command[2])] = gift
        else:
            continue

    elif action == 'JustInCase':
        lst_gifts[-1] = gift

lst_gifts = [i for i in lst_gifts if i != 'None']
print(' '.join(lst_gifts))


# ______________ version 4 __________________100% judge


gifts = input().split(' ')

while True:
    command = input()
    if command == 'No Money':
        break

    command = command.split(' ')

    if command[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = 'None'

    elif command[0] == 'Required':
        if 0 <= int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

for j in gifts:
    if 'None' in gifts:
        gifts.remove('None')

print(' '.join(gifts))


# ______________ version 3 __________________100% judge


gifts = input().split(' ')

while True:
    command = input()
    if command == 'No Money':
        break

    command = command.split(' ')

    if command[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = 'None'

    elif command[0] == 'Required':
        if 0 <= int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))


# ______________ version 2 __________________100 % in judge


gifts = input().split(' ')

while True:
    command = input()
    if command == 'No Money':
        break

    elif command[:10] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == command[11:]:
                gifts[i] = 'None'

    elif command[:8] == 'Required':
        com_1 = command.split(' ')
        if 0 <= int(com_1[2]) < len(gifts):
            gifts[int(com_1[2])] = com_1[1]

    elif command[:10] == "JustInCase":
        gifts[-1] = command[11:]

for j in range(len(gifts)):
    if 'None' in gifts:
        gifts.remove('None')

print(' '.join(gifts))


# ______________ version 1 __________________ 100% in judge


gifts = input().split(' ')

while True:
    command = input()
    if command == 'No Money':
        break

    command = command.split(' ')

    if command[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = 'None'

    elif command[0] == 'Required':
        if 0 <= int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

for j in range(len(gifts)):
    if 'None' in gifts:
        gifts.remove('None')

print(' '.join(gifts))
