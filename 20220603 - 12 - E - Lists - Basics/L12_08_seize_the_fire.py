# 22020603 - Python - L12 - Lists Basics - Exercise
# 08 - Seize The Fire - https://judge.softuni.org/Contests/Compete/Index/1725#7


# _____________________ version 1 ______________________ judge 100%


str_in = input().split('#')
water = int(input())

effort = 0
result = ''
total_fire = 0
temp = ''

for i in range(len(str_in)):
    if 'High' in str_in[i]:
        cell_value = int(str_in[i][7:])
        if 81 <= cell_value <= 125 and water >= cell_value:
            water -= cell_value
            total_fire += cell_value
            temp = f'\n - {cell_value}'

    elif 'Medium' in str_in[i]:
        cell_value = int(str_in[i][9:])
        if 51 <= cell_value <= 80 and water >= cell_value:
            water -= cell_value
            total_fire += cell_value
            temp = f'\n - {cell_value}'

    elif 'Low' in str_in[i]:
        cell_value = int(str_in[i][6:])
        if 1 <= cell_value <= 50 and water >= cell_value:
            water -= cell_value
            total_fire += cell_value
            temp = f'\n - {cell_value}'

    if temp == '':
        continue

    result += f' {temp}'
    temp = ''

print(f'Cells: {result}')
print(f'Effort: {total_fire * 0.25:.2f}')
print(f'Total Fire: {total_fire}')


# ________________ version 2 ________________________ judge 100%


str_in = input().split('#')
water = int(input())

effort = 0
result = ''
total_fire = 0
temp = ''

for i in range(len(str_in)):
    cell = str_in[i].split(' = ')
    level = cell[0]
    value = int(cell[1])

    if 'High' in str_in[i] and 81 <= value <= 125 and water >= value:
        water -= value
        total_fire += value
        temp = f'\n - {value}'

    elif 'Medium' in str_in[i] and 51 <= value <= 80 and water >= value:
        water -= value
        total_fire += value
        temp = f'\n - {value}'

    elif 'Low' in str_in[i] and 1 <= value <= 50 and water >= value:
        water -= value
        total_fire += value
        temp = f'\n - {value}'

    if temp == '':
        continue

    result += f' {temp}'
    temp = ''

print(f'Cells: {result}')
print(f'Effort: {total_fire * 0.25:.2f}')
print(f'Total Fire: {total_fire}')


# ________________ version 3 ________________________ judge 100%


fires = input().split('#')
water_inStock = int(input())
total_effort = 0
cells_putout = []

for i in fires:
    cell = i.split(' = ')
    c_level = cell[0]
    c_value = int(cell[1])

    if (c_level == 'High') and (81 <= c_value <= 125) and water_inStock >= c_value:
        water_inStock -= c_value
        total_effort += c_value * 0.25
        cells_putout.append(c_value)

    elif (c_level == 'Medium') and (51 <= c_value <= 80) and water_inStock >= c_value:
        water_inStock -= c_value
        total_effort += c_value * 0.25
        cells_putout.append(c_value)

    elif (c_level == 'Low') and (1 <= c_value <= 50) and water_inStock >= c_value:
        water_inStock -= c_value
        total_effort += c_value * 0.25
        cells_putout.append(c_value)

print(f'Cells:')

for i in range(len(cells_putout)):
    print(f' - {cells_putout[i]}')

print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {sum(cells_putout)}')


""" _______________ Seize The Fire ________________


The group of adventurists has gone on their first task. Now they should walk through fire - literally.
They should use all the water they have left. Your task is to help them survive.

Create a program that calculates the water needed to put out a "fire cell",
based on the given information about its "fire level" and how much it gets affected by water.
First, you will be given the level of fire inside the cell with the integer value of the cell,
which represents the needed water to put out the fire.

They will be given in the following format:

"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … 
{typeOfFire} = {valueOfCell}"

Afterward you will receive the amount of water you have for putting out the fires.
There is a range of fire for each fire type, and if a cell's value is below or exceeds it, it is invalid,
and you do not need to put it out.

Type of Fire:	Range:
------------    -----
High	        81 - 125
Medium	        51 - 80
Low	            1 – 50

If a cell is valid, you should put it out by reducing the water with its value.
Putting out fire also takes effort, and you need to calculate it.
Its value is equal to 25% of the cell's value.
In the end, you will have to print the total effort.
Keep putting out cells until you run out of water.
Skip it and try the next one if you do not have enough water to put out a given cell.
In the end, print the cells you have put out in the following format:

"Cells:
 - {cell1}
 - {cell2}
 …
 - {cellN}"

"Effort: {effort}"

The effort should be formatted to the second decimal place.
In the end, print the total fire you have put out from all the cells in the following format: 

"Total Fire: {total_fire}"


Input / Constraints:
-------------------
•	On the 1st line, you will receive the fires with their cells in the format described above – integer numbers in the range [1…500].
•	On the 2nd line, you will receive the water – an integer number in the range [0….100000].


Output:
------
Print the output as described above.


____________ Test Data ______________


Input 1:
-------
High = 89#Low = 28#Medium = 77#Low = 23
1250


Output 1:
--------
Cells:
 - 89
 - 28
 - 77
 - 23
Effort: 54.25
Total Fire: 217


-------------------------------------


Input 2:
-------
High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77
220


Output 2:
--------
Cells:
 - 40
 - 110
Effort: 37.50
Total Fire: 150


-------------------------------------
"""
