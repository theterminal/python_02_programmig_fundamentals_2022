# 22020603 - Python - L12 - Lists Basics - Exercise
# 07 - Easter Gifts - https://judge.softuni.org/Contests/Compete/Index/1725#6


# ______________ version 5 _________________ judge 100%


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


# ______________ version 4 __________________ judge 100%


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


# ______________ version 3 __________________ judge 100%


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


# ______________ version 2 __________________ judge 100%


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


# ______________ version 1 __________________ judge 100%


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


""" _______________ Easter Gifts __________________


As a good friend, you decide to buy presents for your friends.
Create a program that helps you plan the gifts for your friends and family.

First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:

"{gift1} {gift2} {gift3}… {giftn}"

Then you will start receiving commands until you read the "No Money" message.
There are three possible commands:

    •	"OutOfStock {gift}"
        o	Find the gifts with this name in your collection, if any, and change their values to "None".
        
    •	"Required {gift} {index}"
        o	If the index is valid, replace the gift on the given index with the given gift.
        
    •	"JustInCase {gift}"
        o	Replace the value of your last gift with this one.

In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:

"{gift1} {gift2} {gift3} … {giftn}"


Input / Constraints:
-------------------
    •	On the 1st line,  you will receive the names of the gifts, separated by a single space.
    •	On the following lines, until the "No Money" command is received, you will be receiving commands.
    •	The input will always be valid.


Output:
------
    •	Print the gifts in the format described above.


___________________ Test Data _____________________


Input 1:
-------
Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
OutOfStock Eggs
Required Spoon 2
JustInCase ChocolateEgg
No Money


Output 1:
--------
StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg


---------------------------------------------------


Input 2:
-------
Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes
Required Paper 8
OutOfStock Clothes
Required Chocolate 2
JustInCase Hat
OutOfStock Cable
No Money


Output 2:
--------
Sweets Cozonac Chocolate Flowers Wine Eggs Hat


---------------------------------------------------
"""
