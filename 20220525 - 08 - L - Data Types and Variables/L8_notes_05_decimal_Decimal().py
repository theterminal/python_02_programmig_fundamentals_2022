# 20220608 - Python Code
# 'while loop' some syntax, and decimal module

import decimal


# -----------------------------------------------------------
# It'll print every iteration while 'n' > 0, and then it'll print the 'print' statement inside the 'else' statement!

print('\n------------ Example 1 -----------------\n')
print('It\'ll print every iteration while \'n\' > 0, and then it\'ll print the \'print\' statement inside the \'else\' statement!\n')


n = 5
counter = 0

while n:
    counter += 1
    print(f'n = {n} from \'while n\' -> iteration # {counter}')
    n -= decimal.Decimal(0.1)
    n = round(n, 1)
else:
    counter += 1
    print(f'n = {n} from \'the \'else\' of the while n\' -> iteration # {counter}')


# ----------------------------------------------------------
# It will print only the 'else' 'print' statement when 'n == 0'


print('\n------------ Example 2 -----------------\n')
print('It will print only the \'else\' \'print\' statement when \'n == 0\'\n')


n = 10
counter = 0

while not n:
    counter += 1
    print(f'n = {n} from \'while n\' -> iteration # {counter}')
    n -= 0.1
    n = round(n, 1)
else:
    counter += 1
    print(f'n = {n} from \'the \'else\' of the while n\' -> iteration # {counter}')


# ----------------------------------------------------------


print('\n------------ Example 3 -----------------\n')

float_division = 4/3
decimal_division = decimal.Decimal(4) / decimal.Decimal(3)

print(f'Result for float division of 4 by 3: {float_division}\n')

print(f'Result for decimal division of 4 by 3: {decimal_division}\n')

print(decimal.getcontext())


# ----------------------------------------------------------


print('\n------------ Example 4 -----------------\n')

num_1 = decimal.Decimal(4)
num_2 = decimal.Decimal(3)

print("First number is:", num_1)
print("Second number is:", num_2, '\n')
num_3 = num_1 / num_2

print("num_1 divided by num_2 is:", num_3)
num_4 = round(num_3, 2)
print("Rounded value upto two decimal points is:", num_4)


# -----------------------------------------------------------


print('\n------------ Example 5 -----------------\n')

x = decimal.Decimal('1.2')
y = decimal.Decimal('2.2')
z = decimal.Decimal('3.4')
a = x + y

print('x:', x)
print('y:', y)
print('z:', z)
print('\nx + y: = ', a)
print('(x + y == z) =', a == z)
