# 20220727 - Python - Exam Preparation
# 01 - Password Reset - judge url: https://judge.softuni.org/Contests/Practice/Index/2303#0


# ------------------------- version 1 ---------- no function --------- judge: 100%


data = input()

while True:
    command = input()
    if command == 'Done':
        break

    command = command.split(' ')
    action = command[0]

    if action == 'TakeOdd':
        new_pass = ''
        for i in range(1, len(data), 2):
            new_pass += data[i]
        data = new_pass
        print(data)

    elif action == 'Cut':
        index = int(command[1])
        length = int(command[2])

        data = data[:index] + data[index + length:]
        print(data)

    elif action == 'Substitute':
        old_string = command[1]
        new_string = command[2]

        if old_string in data:
            data = data.replace(old_string, new_string)
            print(data)
        else:
            print('Nothing to replace!')

print(f'Your password is: {data}')


# ------------------------- version 2 ------ with function ------- judge: 100%


def password_reset():
    data = input()

    while True:
        command = input()
        if command == 'Done':
            break

        command = command.split(' ')
        action = command[0]

        if action == 'TakeOdd':
            new_pass = ''
            for i in range(1, len(data), 2):
                new_pass += data[i]
            data = new_pass
            print(data)

        elif action == 'Cut':
            index = int(command[1])
            length = int(command[2])

            data = data[:index] + data[index + length:]
            print(data)

        elif action == 'Substitute':
            old_string = command[1]
            new_string = command[2]

            if old_string in data:
                data = data.replace(old_string, new_string)
                print(data)
            else:
                print('Nothing to replace!')

    print(f'Your password is: {data}')


password_reset()


""" ---------------- Password Reset -------------------


Yet again, you have forgotten your password.
Naturally, it's not the first time this has happened.
Actually, you got so tired of it that you decided to help yourself with an intelligent solution.

Write a password reset program that performs a series of commands upon a predefined string.
First, you will receive a string, and afterward, until the command "Done" is given,
you will be receiving strings with commands split by a single space. The commands will be the following:

    •	"TakeOdd"
        o	 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.

    •	"Cut {index} {length}"
        o	Gets the substring with the given length starting from the given index from the password and removes its first occurrence, then prints the password on the console.
        o	The given index and the length will always be valid.

    •	"Substitute {substring} {substitute}"
        o	If the raw password contains the given substring, replaces all of its occurrences with the substitute text given and prints the result.
        o	If it doesn't, prints "Nothing to replace!".


Input:
-----
    •	You will be receiving strings until the "Done" command is given.

Output:
------
    •	After the "Done" command is received, print:
        o	"Your password is: {password}"

Constraints:
-----------
    •	The indexes from the "Cut {index} {length}" command will always be valid.


---------------- Test Data -------------------


Input 1:
-------
Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr 
TakeOdd
Cut 15 3
Substitute :: -
Substitute | ^
Done


Output 1:
--------
icecream::hot::summer
icecream::hot::mer
icecream-hot-mer
Nothing to replace!
Your password is: icecream-hot-mer


----------------------------------------------


Input 2:
-------
up8rgoyg3r1atmlmpiunagt!-irs7!1fgulnnnqy
TakeOdd
Cut 18 2
Substitute ! ***
Substitute ? .!.
Done


Output 2:
--------
programming!is!funny
programming!is!fun
programming***is***fun
Nothing to replace!
Your password is: programming***is***fun


----------------------------------------------
"""
