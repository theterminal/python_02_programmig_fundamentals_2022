# 22020613 - Python - L12 - Lists Basics - Exercise
# 10 - Bread Factory - https://judge.softuni.org/Contests/Compete/Index/1725#9


# ------------- version 2 --------------------------- judge 100%


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


# ------------- version 1 --------------------------- judge 100%


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


""" ________________ Bread Factory _________________


As a young baker, you are baking the bread out of the bakery. 

You have initial energy 100 and initial coins 100.
You will be given a string representing the working day events.
Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")

•	If the event is "rest":
    o	You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100).
        Print: "You gained {gained_energy} energy.". 
    o	After that, print your current energy: "Current energy: {current_energy}.".

•	If the event is "order": 
    o	You've earned some coins (the number in the second part).
    o	Each time you get an order, your energy decreases by 30 points.
        	If you have the energy to complete the order, print: "You earned {earned} coins.".
        	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".

•	In any other case, you have an ingredient you should buy. The second part of the event contains the coins you should spend. 
    o	If you have enough money, you should buy the ingredient and print: "You bought {ingredient}."
    o	Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.

If you managed to handle all events throughout the day, print on the following 3 lines: 
"Day completed!"
"Coins: {coins}"
"Energy: {energy}"


Input / Constraints:
-------------------
You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
"event1|event2| … eventN".

Each event contains an event name or an ingredient and a number, separated by a dash in the format:
"{event/ingredient}-{number}"


Output:
------
Print the corresponding messages described above.


_________________ Test Data _________________


Input 1:
-------
rest-2|order-10|eggs-100|rest-10


Output 1:
--------
You gained 0 energy.
Current energy: 100.
You earned 10 coins.
You bought eggs.
You gained 10 energy.
Current energy: 80.
Day completed!
Coins: 10
Energy: 80


--------------------------------------------


Input 2:
-------
order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000


Output 2:
--------
You earned 10 coins.
You earned 10 coins.
You earned 10 coins.
You bought flour.
You had to rest!
Closed! Cannot afford oven.


--------------------------------------------
"""
