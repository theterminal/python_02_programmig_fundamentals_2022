# 22020603 - Python Code - L12 - Lists Basics - Exercise
# 08 - Seize The Fire - https://judge.softuni.org/Contests/Compete/Index/1725#7

# _____________________ version 1 -------------------------------

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

# ________________ version 2 ________________________

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