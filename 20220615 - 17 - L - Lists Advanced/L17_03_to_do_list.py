# 20220616 - Python Code - Lists Advance - Lecture
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
