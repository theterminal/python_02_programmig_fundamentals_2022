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


"""----------------- Furniture ---------------------


Write a program that calculates the total cost of bought furniture.
You will be given information about each purchase on separate lines until you receive the command "Purchase". 

Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}".

The price could be a floating-point or integer number.

You should store the names of the furniture and the total price. 
In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:


"Bought furniture:
{1st name}
{2nd name}
…
{N name}
Total money spend: {total_cost}"


------------------- Examples --------------------


Input 1:
--------
>>Sofa<<312.23!3
>>TV<<300!5
>Invalid<<!5
Purchase


Output 1:
---------
Bought furniture:
Sofa
TV
Total money spend: 2436.69


-------------------------------------


Input 2:
--------
>Invalid<<!5
>Invalid<<!5
>Invalid<<!5
Purchase


Output 2:
---------
Bought furniture:
Total money spend: 0.00


"""