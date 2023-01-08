# 20220714 - Python - Dictionaries - Exercise
# 05 - Legendary Farming - judge url: https://judge.softuni.org/Contests/Compete/Index/1737#4


# ---------------------- version 3 ------------------ judge: 100%


dct_1 = {'shards': 0, 'fragments': 0, 'motes': 0}
flag = 0

while True:
    data_in = input().split(' ')
    for i in range(0, len(data_in), 2):
        material = data_in[i + 1].lower()
        quantity = int(data_in[i])

        if material == 'shards' or material == 'fragments' or material == 'motes':
            dct_1[material] += quantity
            if dct_1['shards'] >= 250:
                print('Shadowmourne obtained!')
                dct_1[material] -= 250
                flag = 1
                break
            elif dct_1['fragments'] >= 250:
                print('Valanyr obtained!')
                dct_1[material] -= 250
                flag = 1
                break
            elif dct_1['motes'] >= 250:
                print('Dragonwrath obtained!')
                dct_1[material] -= 250
                flag = 1
                break
        else:
            if material not in dct_1:
                dct_1[material] = 0
            dct_1[material] += quantity

    if flag == 1:
        break

for k, v in dct_1.items():
    print(f'{k}: {v}')


# ---------------------- version 2 ------------------ judge: 100%


dct_goods = {'shards': 0, 'fragments': 0, 'motes': 0}
dct_junk = {}
flag = 0

while True:
    data_in = input().split(' ')
    for i in range(0, len(data_in), 2):
        material = data_in[i + 1].lower()
        quantity = int(data_in[i])

        if material == 'shards' or material == 'fragments' or material == 'motes':
            dct_goods[material] += quantity
            if dct_goods['shards'] >= 250:
                print('Shadowmourne obtained!')
                dct_goods[material] -= 250
                flag = 1
                break
            elif dct_goods['fragments'] >= 250:
                print('Valanyr obtained!')
                dct_goods[material] -= 250
                flag = 1
                break
            elif dct_goods['motes'] >= 250:
                print('Dragonwrath obtained!')
                dct_goods[material] -= 250
                flag = 1
                break
        else:
            if material not in dct_junk:
                dct_junk[material] = 0
            dct_junk[material] += quantity

    if flag == 1:
        break

for k, v in dct_goods.items():
    print(f'{k}: {v}')

for k, v in dct_junk.items():
    print(f'{k}: {v}')


# ---------------------- version 1 ------------------ judge: 100%


dct = {}
flag = 0

while True:
    data_in = input().split(' ')
    for i in range(0, len(data_in), 2):
        quantity = int(data_in[i])
        material = data_in[i + 1].lower()

        if material not in dct.keys():
            dct[material] = 0
        dct[material] += quantity

        for material in dct.keys():
            if material == 'shards' and dct['shards'] >= 250:
                print(f'Shadowmourne obtained!')
                dct[material] -= 250
                flag = 1
                break
            elif material == 'fragments' and dct['fragments'] >= 250:
                print(f'Valanyr obtained!')
                dct[material] -= 250
                flag = 1
                break
            elif material == 'motes' and dct['motes'] >= 250:
                print(f'Dragonwrath obtained!')
                dct[material] -= 250
                flag = 1
                break

        if flag == 1:
            break

    if flag == 1:
        break

if 'shards' in dct.keys():
    print(f'shards: {dct["shards"]}')
    dct.pop('shards')
else:
    print('shards: 0')

if 'fragments' in dct.keys():
    print(f'fragments: {dct["fragments"]}')
    dct.pop('fragments')
else:
    print('fragments: 0')

if 'motes' in dct.keys():
    print(f'motes: {dct["motes"]}')
    dct.pop('motes')
else:
    print('motes: 0')

for k, v in dct.items():
    print(f'{k}: {v}')
