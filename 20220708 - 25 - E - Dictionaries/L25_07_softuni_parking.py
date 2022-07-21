# 20220714 - Python Code - Dictionaries - Exercise
# 07 - SoftUni Parking - judge url: https://judge.softuni.org/Contests/Compete/Index/1737#6


# ---------------------------- version 1 ----------------------------- judge: 100%


num_commands = int(input())
db = {}

for i in range(num_commands):
    command = input().split(' ')

    name = command[1]

    if len(command) == 3:
        l_plate = command[2]
        if name in db:
            print(f'ERROR: already registered with plate number {l_plate}')
        else:
            db[name] = l_plate
            print(f'{name} registered {l_plate} successfully')
    else:
        if name not in db:
            print(f'ERROR: user {name} not found')
        else:
            db.pop(name)
            print(f'{name} unregistered successfully')

for k, v in db.items():
    print(f'{k} => {v}')
