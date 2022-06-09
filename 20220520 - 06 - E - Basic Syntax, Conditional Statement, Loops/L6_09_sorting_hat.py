# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 09 - Sorting Hat - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#8

house_to_stay_in, flag = '', 0

while True:
    guest_name_entered = input()

    if guest_name_entered == 'Welcome!':
        flag = 1
        break

    if guest_name_entered == 'Voldemort':
        flag = 2
        break

    length_guest_name_entered = len(guest_name_entered)

    if length_guest_name_entered < 5:
        house_to_stay_in = 'Gryffindor.'
    elif length_guest_name_entered == 5:
        house_to_stay_in = 'Slytherin.'
    elif length_guest_name_entered == 6:
        house_to_stay_in = 'Ravenclaw.'
    elif length_guest_name_entered > 6:
        house_to_stay_in = 'Hufflepuff.'

    print(f'{guest_name_entered} goes to {house_to_stay_in}')

if flag == 1:
    print('Welcome to Hogwarts.')
elif flag == 2:
    print('You must not speak of that name!')
