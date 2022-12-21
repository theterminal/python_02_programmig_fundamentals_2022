# 20220805 - Python - Old Exams
# 03 - P!rates - judge url: https://judge.softuni.org/Contests/Practice/Index/2302#2


# ------------------------- version 2 ------------------------ judge: 100%


def loading():
    info_dict = {}                      # info_dict = {town: [population, gold]}

    while True:
        data = input()
        if data == 'Sail':
            break

        town, population, gold = data.split('||')

        if town not in info_dict:
            info_dict[town] = [int(population), int(gold)]
            continue
        info_dict[town][0] += int(population)
        info_dict[town][1] += int(gold)

    return info_dict


def action(info_dict):
    while True:
        event = input()
        if event == 'End':
            break

        event = event.split('=>')
        activity = event[0]
        town = event[1]

        if activity == 'Plunder':
            people = int(event[2])
            gold = int(event[3])

            for k, v in info_dict.items():
                if k == town:
                    v[0] -= people
                    v[1] -= gold
                    print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')

            if info_dict[town][0] <= 0 or info_dict[town][1] <= 0:
                del info_dict[town]
                print(f'{town} has been wiped off the map!')

        elif activity == 'Prosper':
            gold = int(event[2])

            if gold <= 0:
                print(f'Gold added cannot be a negative number!')
            else:
                for k, v in info_dict.items():
                    if k == town:
                        v[1] += gold
                        print(f'{gold} gold added to the city treasury. {k} now has {v[1]} gold.')

    return info_dict


def output(info_dict):
    if info_dict:
        print(f'Ahoy, Captain! There are {len(info_dict)} wealthy settlements to go to:')

        for town, pop_gold in info_dict.items():
            print(f'{town} -> Population: {pop_gold[0]} citizens, Gold: {pop_gold[1]} kg')
    else:
        print('Ahoy, Captain! All targets have been plundered and destroyed!')


def pyrates():
    # info_dict = {town: [population, gold]}
    info_dict = loading()
    action(info_dict)
    output(info_dict)


pyrates()


# ------------------------- version 2 ------------------------ judge: 100%


info_dict = {}

while True:
    command = input()
    if command == 'Sail':
        break

    town, population, gold = command.split('||')

    if town not in info_dict:
        info_dict[town] = [int(population), int(gold)]
        continue
    info_dict[town][0] += int(population)
    info_dict[town][1] += int(gold)

while True:
    new_command = input()
    if new_command == 'End':
        break

    new_command = new_command.split('=>')
    town = new_command[1]

    if new_command[0] == 'Plunder':
        people = int(new_command[2])
        gold = int(new_command[3])

        for key, value in info_dict.items():
            if key == town:
                value[0] -= people
                value[1] -= gold
                print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')

        if info_dict[town][0] <= 0 or info_dict[town][1] <= 0:
            del info_dict[town]
            print(f'{town} has been wiped off the map!')

    elif new_command[0] == 'Prosper':
        gold = int(new_command[2])

        if gold <= 0:
            print('Gold added cannot be a negative number!')
        else:
            for key, value in info_dict.items():
                if key == town:
                    value[1] += gold
                    print(f'{gold} gold added to the city treasury. {key} now has {value[1]} gold.')

if info_dict:
    print(f'Ahoy, Captain! There are {len(info_dict)} wealthy settlements to go to:')
    for key, value in info_dict.items():
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
