# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 09 - Sorting Hat - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#8


# -------------------------- version 1 ---------------------------- judge: 100%


house_to_stay_in = ''

while True:
    guest_name = input()

    if guest_name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break

    if guest_name == 'Voldemort':
        print('You must not speak of that name!')
        break

    if len(guest_name) < 5:
        house_to_stay_in = 'Gryffindor.'
    elif len(guest_name) == 5:
        house_to_stay_in = 'Slytherin.'
    elif len(guest_name) == 6:
        house_to_stay_in = 'Ravenclaw.'
    elif len(guest_name) > 6:
        house_to_stay_in = 'Hufflepuff.'

    print(f'{guest_name} goes to {house_to_stay_in}')
