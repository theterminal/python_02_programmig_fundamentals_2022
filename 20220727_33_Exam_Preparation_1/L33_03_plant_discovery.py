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
