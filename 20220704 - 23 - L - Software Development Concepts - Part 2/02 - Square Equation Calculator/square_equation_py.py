# 20220625 - Square Equation

import math


print('\nWelcome to 02 - Square Equation Calculator\n')

num_x2 = int(input('Enter the num before x2: '))
num_x = int(input('Enter the num before x: '))
num = int(input('Enter the free num: '))

print('\n----------------------------------------')

if num_x2 == 1:
    if num_x > 0 and num > 0:
        print(f'x2 + {num_x}x + {num} = 0')
    elif num_x > 0 and num < 0:
        print(f'x2 + {num_x}x - {abs(num)} = 0')
    elif num_x < 0 and num > 0:
        print(f'x2 - {abs(num_x)}x + {num} = 0')
    elif num_x < 0 and num < 0:
        print(f'x2 - {abs(num_x)}x - {abs(num)} = 0')
elif num_x2 == -1:
    if num_x > 0 and num > 0:
        print(f'-x2 + {num_x}x + {num} = 0')
    elif num_x > 0 and num < 0:
        print(f'-x2 + {num_x}x - {abs(num)} = 0')
    elif num_x < 0 and num > 0:
        print(f'-x2 - {abs(num_x)}x + {num} = 0')
    elif num_x < 0 and num < 0:
        print(f'-x2 - {abs(num_x)}x - {abs(num)} = 0')
else:
    if num_x2 == 0:
        print('The equation is NOT a quadratic equation!')
        exit()
    else:
        if num_x >= 0:
            if num >= 0:
                print(f'{num_x2}x2 + {num_x}x + {num} = 0')
            else:
                print(f'{num_x2}x2 + {num_x}x - {abs(num)} = 0')
        else:
            if num >= 0:
                print(f'{num_x2}x2 - {abs(num_x)}x + {num} = 0')
            else:
                print(f'{num_x2}x2 - {abs(num_x)}x - {abs(num)} = 0')

disc = (num_x * num_x) - (4 * num_x2 * num)

print('----------------------------------------')
if disc < 0:
    print(f'Discriminant \'D\' = {disc}, and is \'< 0\'   =>   The equation has no real solutions')

elif disc == 0:
    print(f'Discriminant \'D\' = 0   =>   The equation has 1 real solution - \'x1\'')
    x1 = (- num_x + math.sqrt(disc)) / 2 * num_x2
    print(f'\nx1 = {x1}')
    print('\n----------------------------------------\n')
    print(f'x1 = ({-num_x} + √{disc}) / {2 * num_x2}')

else:
    print(f'Discriminant \'D\' = {disc}, and is \'> 0\'   =>   The equation has 2 real solutions')
    x1 = (- num_x + math.sqrt(disc)) / 2 * num_x2
    x2 = (- num_x - math.sqrt(disc)) / 2 * num_x2

    print(f'\nx1 = {x1}\nx2 = {x2}')

    print('----------------------------------------\n')
    print('Raw format for x1 and x2:')
    print(f'x1 = ({-num_x} + √{disc}) / {2 * num_x2}')
    print(f'x2 = ({-num_x} - √{disc}) / {2 * num_x2}')

print('\n----------------------------------------\n')