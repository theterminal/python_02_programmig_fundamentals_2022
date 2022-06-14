# 22020603 - Python Code - L12 - Lists Basics - Exercise
# 07 - Easter Gifts - https://judge.softuni.org/Contests/Compete/Index/1725#6


# ______________ version 5 __________________100% judge

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

# ______________ version 3 __________________ 100% in judge


# gifts = input().split(' ')
#
# while True:
#     command = input()
#     if command == 'No Money':
#         break
#
#     command = command.split(' ')
#
#     if command[0] == 'OutOfStock':
#         for i in range(len(gifts)):
#             if gifts[i] == command[1]:
#                 gifts[i] = 'None'
#
#     elif command[0] == 'Required':
#         if 0 <= int(command[2]) < len(gifts):
#             gifts[int(command[2])] = command[1]
#
#     elif command[0] == "JustInCase":
#         gifts[-1] = command[1]
#
# for j in range(len(gifts)):
#     if 'None' in gifts:
#         gifts.remove('None')
#
# print(' '.join(gifts))


# ________________ version 1 __________________________ 70% in judge


# that is the end part only!!!
#
# for j in gifts:
#     if j == 'None':
#         gifts.remove('None')
#
# print(' '.join(gifts))
