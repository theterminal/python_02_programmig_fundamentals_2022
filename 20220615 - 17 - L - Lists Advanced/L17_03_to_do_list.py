# 20220616 - Python - Lists Advance - Lecture
# 03 - To-Do List - judge: https://judge.softuni.org/Contests/Practice/Index/1730#2


# -------------- version 3 -------------- 100% judge


tasks = []

while True:
    command = input().split('-')
    if command[0] == 'End':
        break

    rank = int(command[0])
    task = command[1]
    tasks.append((rank, task))

print([x[1] for x in sorted(tasks)])


# -------------- version 2 -------------- 100% judge


lst_full = ['0'] * 10

while True:
    command = input()
    if command == 'End':
        break

    pair = command.split('-')
    lst_full.pop(int(pair[0]))
    lst_full.insert(int(pair[0]), pair[1])

print([x for x in lst_full if x != '0'])


# # --------------- version 1 ------------- 80% judge


lst_full = []
result = []

while True:
    command = input()
    if command == 'End':
        break

    lst_full += [command]
    lst_full.sort()

for i in range(len(lst_full)):
    result.append(lst_full[i][2::])

print(result)


""" ___________________ To Do List ___________________


You will be receiving to-do notes until you get the command "End".
The notes will be in the format: "{importance}-{note}". 
Return a list containing all to-do notes sorted by importance in ascending order.
The importance value will always be an integer between 1 and 10 (inclusive).


___________ Test Data ___________


Input 1:
-------
2-Walk the dog
1-Drink coffee
6-Dinner
5-Work
End


Output 1:
--------
['Drink coffee', 'Walk the dog', 'Work', 'Dinner']


---------------------------------


Input 2:
-------
3-C
2-A
1-B
6-V
End


Output 2:
--------
['B', 'A', 'C', 'V']


---------------------------------
"""
