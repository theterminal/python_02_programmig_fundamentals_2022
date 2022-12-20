# 20220722 - Python Code - Regular Expressions - Exercise
# 05 - Furniture - judge url: https://judge.softuni.org/Contests/Compete/Index/1743#4

import re
# use this to construct the regex: https://regex101.com/


# ------------------------ version 1 -------------------- judge: 100%


pattern = r'>>([A-za-z]+)<<(\d+\.?\d*)\!(\d+)'
total_cost = 0
bought_furniture = []

while True:
    command = input()
    if command == 'Purchase':
        break

    match = re.search(pattern, command)
    if match:
        name, price, quantity = match.groups()
        bought_furniture.append(name)
        total_cost += int(quantity) * float(price)
print('Bought furniture:')

for name in bought_furniture:                                   # when used "''.join(match) instead 'for' loop - judge gav an error. It's judge's problem but good to know
    print(name)

print(f'Total money spend: {total_cost:.2f}')


# ------------------------ version 2 -------------------- judge: 100%


pattern_1 = r'>>([A-za-z]+)<<'
pattern_2 = r'<<(\d+\.?\d*)\!'
pattern_3 = r'!(\d+)'
total_cost = 0
bought_furniture = []

while True:
    command = input()
    if command == 'Purchase':
        break

    match_1 = re.search(pattern_1, command)
    match_2 = re.search(pattern_2, command)
    match_3 = re.search(pattern_3, command)

    if match_1 and match_2 and match_3:
        bought_furniture.append(match_1.group(1))
        total_cost += float(match_2.group(1)) * int(match_3.group(1))

print(f'Bought furniture:')

for name in bought_furniture:
    print(name)

print(f'Total money spend: {total_cost:.2f}')
