# 20220802 - Python Code - Exam Preparation
# 03 - Plant Discovery - judge url: https://judge.softuni.org/Contests/Practice/Index/2518#2


# ------------------------- version 1 ------------------------ judge: 100%


def create_plants(num, plants):
    for _ in range(num):
        data = input().split('<->')
        name = data[0]
        rarity = int(data[1])

        if name not in plants:
            plants[name] = {
                'rarity': rarity,
                'rating': []
            }
        else:
            plants[name]['rarity'] += rarity

    return plants


def additional_data(plants):
    while True:
        command = input().split(': ')
        if command[0] == 'Exhibition':
            break

        action = command[0]
        data = command[1].split(' - ')
        name = data[0]

        if name not in plants:
            print('error')
            continue

        if action == 'Rate':
            rating = int(data[1])
            plants[name]['rating'].append(rating)

        elif action == 'Update':
            new_rarity = int(data[1])
            plants[name]['rarity'] = new_rarity

        elif action == 'Reset':
            plants[name]['rating'].clear()

    return plants


def output(plants):
    print('Plants for the exhibition:')

    for name in plants:
        if len(plants[name]['rating']) > 0 or sum(plants[name]['rating']) > 0:
            av_rating = sum(plants[name]['rating']) / len(plants[name]['rating'])
        else:
            av_rating = 0

        print(f'- {name}; Rarity: {plants[name]["rarity"]}; Rating: {av_rating:.2f}')


def plant_discovery():
    n = int(input())
    plants = {}

    create_plants(n, plants)
    additional_data(plants)
    output(plants)


plant_discovery()


# --------------------------- version 2 --------------------- judge 100%


n = int(input())
plants = {}

for i in range(n):
    data = input().split('<->')
    name = data[0]
    plants[name] = {
        'rarity': int(data[1]),
        'rating': []
    }

while True:
    command = input().split(': ')
    if command[0] == 'Exhibition':
        break

    action = command[0]
    name_rating = command[1].split(' - ')
    name = name_rating[0]

    if name not in plants:
        print('error')
        continue

    if action == 'Rate':
        rating = int(name_rating[1])
        plants[name]['rating'].append(rating)

    elif action == 'Update':
        new_rarity = int(name_rating[1])
        plants[name]['rarity'] = new_rarity

    elif action == 'Reset':
        plants[name]['rating'].clear()

print('Plants for the exhibition:')

for k, v in plants.items():
    if len(v['rating']) > 0 or sum(v['rating']) > 0:
        av_rating = sum(v['rating']) / len(v['rating'])
    else:
        av_rating = 0

    print(f'- {k}; Rarity: {v["rarity"]}; Rating: {av_rating:.2f}')


""" ------------------ Plant Discovery ----------------------


You have now returned from your world tour.
On your way, you have discovered some new plants,
and you want to gather some information about them and create an exhibition to see which plant is highest rated.

On the first line, you will receive a number 'n'.
On the next 'n' lines, you will be given some information about the plants that you have discovered in the format:

"{plant}<->{rarity}".

Store that information because you will need it later.
If you receive a plant more than once, update its rarity.

After that, until you receive the command "Exhibition", you will be given some of these commands:

    •	"Rate: {plant} - {rating}"          – add the given rating to the plant (store all ratings)
    •	"Update: {plant} - {new_rarity}"    – update the rarity of the plant with the new one
    •	"Reset: {plant}"                    – remove all the ratings of the given plant

Note: If any given plant name is invalid, print "error"

After the command "Exhibition", print the information that you have about the plants in the following format:

"Plants for the exhibition:
- {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
- {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
…
- {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"

The average rating should be formatted to the second decimal place.


"""
