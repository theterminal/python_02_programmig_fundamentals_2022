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


''' ---------------- Sorting Hat ------------------


Help out the sorting hat to sort the new students in the houses of Hogwarts.

You will be receiving names until the command "Welcome!".

The length of each name determines in which house the student is going:

    •	If the name is less than 5 chars, the student is going into Gryffindor
        •	Print "{name} goes to Gryffindor."

    •	If the name is exactly 5 chars, the student is going into Slytherin
        •	Print "{name} goes to Slytherin."

    •	If the name is exactly 6 chars, the student is going into Ravenclaw
        •	Print "{name} goes to Ravenclaw."

    •	If the name is more than 6 chars, the student is going into Hufflepuff
        •	Print "{name} goes to Hufflepuff."

While receiving names, if you receive "Voldemort", print:
"You must not speak of that name!" and end the program.

No more sorting for today!

If all students are sorted successfully, print:
"Welcome to Hogwarts."


------------- Test Data ---------------


Input 1:
-------
Harry
Ron
Ginny
Draco
Welcome!


Output 1:
--------
Harry goes to Slytherin.
Ron goes to Gryffindor.
Ginny goes to Slytherin.
Draco goes to Slytherin.
Welcome to Hogwarts.


---------------------------------------


Input 2:
-------
Luna
Hermione
Neville
Voldemort


Output 2:
--------
Luna goes to Gryffindor.
Hermione goes to Hufflepuff.
Neville goes to Hufflepuff.
You must not speak of that name!


'''
