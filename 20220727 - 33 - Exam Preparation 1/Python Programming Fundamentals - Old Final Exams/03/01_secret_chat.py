# 20220730 - Python Code - Exam Preparation
# 01 - Secret Chat - judge url: https://judge.softuni.org/Contests/Practice/Index/2307#0


# ------------------------- version 1 ------------------------ judge: 100%


data = input()

while True:
    command = input()
    if command == 'Reveal':
        break

    command = command.split(':|:')
    action = command[0]

    if action == 'InsertSpace':
        index = int(command[1])
        data = data[:index] + ' ' + data[index:]
        print(data)

    elif action == 'Reverse':
        substring = command[1]

        if substring in data:
            data = data.replace(substring, '', 1)
            substring = substring[::-1]
            data += substring
            print(data)
        else:
            print('error')

    elif action == 'ChangeAll':
        old_substring = command[1]
        new_substring = command[2]

        if old_substring in data:
            data = data.replace(old_substring, new_substring)
            print(data)

print(f'You have a new text message: {data}')


""" ------------------ Secret Chat ----------------------


You have plenty of free time, so you decide to write a program that conceals and reveals your received messages.
Go ahead and type it in!

On the first line of the input, you will receive the concealed message.
After that, until the "Reveal" command is given, you will receive strings with instructions
for different operations that need to be performed upon the concealed message to interpret it and reveal its actual content.

There are several types of instructions, split by ":|:"
    •	"InsertSpace:|:{index}":
        o	Inserts a single space at the given index. The given index will always be valid.

    •	"Reverse:|:{substring}":
        o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
        o	If not, print "error".
        o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.

    •	"ChangeAll:|:{substring}:|:{replacement}":
        o	Changes all occurrences of the given substring with the replacement text.

Input / Constraints:
-------------------
    •	On the first line, you will receive a string with a message.
    •	On the following lines, you will be receiving commands, split by ":|:".

Output:
------
    •	After each set of instructions, print the resulting string.
    •	After the "Reveal" command is received, print this message:
        "You have a new text message: {message}"


--------------- Test Data ------------------


Input 1:
-------
heVVodar!gniV
ChangeAll:|:V:|:l
Reverse:|:!gnil
InsertSpace:|:5
Reveal


Output 1:
--------
hellodar!gnil
hellodarling!
hello darling!
You have a new text message: hello darling!


___________________________________________

"""
