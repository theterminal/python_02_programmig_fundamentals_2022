# 22020613 - Python Code - L12 - Lists Basics - Exercise
# 10 - Bread Factory - https://judge.softuni.org/Contests/Compete/Index/1725#9

# ------------- version 2 ---------------------------

energy = coins = 100
str_in = input().split('|')
flag = False

for i in range(len(str_in)):
    event = str_in[i].split('-')
    event_type = event[0]
    event_num = int(event[1])

    if event_type == 'rest':
        energy += event_num

        if energy <= 100:
            energy_gained = event_num
        else:
            energy_gained = event_num - (energy - 100)
            energy = 100

        print(f'You gained {energy_gained} energy.')
        print(f'Current energy: {energy}.')

    elif event_type == 'order':
        if energy < 30:
            energy += 50
            if energy > 100:
                energy = 100

            print('You had to rest!')
            continue

        coins += event_num
        energy -= 30
        print(f'You earned {event_num} coins.')

    else:
        if coins < event_num:
            print(f'Closed! Cannot afford {event_type}.')
            flag = True
            break

        coins -= event_num
        print(f'You bought {event_type}.')

if not flag:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')

# ------------- version 1 ---------------------------

energy = coins = 100
str_in = input().split('|')
flag = False

for i in range(len(str_in)):
    event = str_in[i].split('-')
    event_type = event[0]
    event_value = int(event[1])

    if 'rest' in event:
        energy_for_event = event_value
        energy_needed_to_100 = 100 - energy

        if energy_for_event <= energy_needed_to_100:
            energy_gained = energy_for_event
        else:
            energy_gained = energy_needed_to_100

        energy += energy_for_event
        if energy > 100:
            energy = 100

        print(f'You gained {energy_gained} energy.')
        print(f'Current energy: {energy}.')

    elif 'order' in event:
        if energy >= 30:
            coins += event_value
            energy -= 30
            print(f'You earned {event_value} coins.')
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print('You had to rest!')
    else:
        if coins >= event_value:
            coins -= event_value
            print(f'You bought {event_type}.')
        else:
            print(f'Closed! Cannot afford {event_type}.')
            flag = True
            break

if not flag:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
