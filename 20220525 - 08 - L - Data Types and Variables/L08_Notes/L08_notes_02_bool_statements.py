# 20220529 - Python - Python Fundamentals - L08 - Data Types and Variables
# notes 02 - Bool


# The values (0, -0, False, '',None) will return 'False' when 'bool' tested!


print('\n------- Example 1 ----------\n')


number = 1

if number:
    print(f'It works! It is a number and the number is: {number}')
else:
    print('else')


print('\n-------- Example 2 ----------\n')


number = None

if number:
    print(f'It is a number! And the number is: {number}')
else:
    print(f'No! It is not a number! Result is: {number}')
