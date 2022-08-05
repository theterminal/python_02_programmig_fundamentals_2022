# 20220730 - Python Code - Exam Preparation
# 01 - The Imitation Game - judge url: https://judge.softuni.org/Contests/Practice/Index/2525#0


# ------------------------- version 1 ------------------------ judge: 100%


data = input()

while True:
    command = input()
    if command == "Decode":
        break

    command = command.split('|')
    action = command[0]

    if action == 'Move':
        n = int(command[1])
        data = data[n:] + data[:n]

    elif action == 'Insert':
        index = int(command[1])
        value = command[2]
        data = data[:index] + value + data[index:]

    elif action == 'ChangeAll':
        substring = command[1]
        new_substring = command[2]
        data = data.replace(substring, new_substring)

print(f'The decrypted message is: {data}')


""" ---------------- The Imitation Game -----------------


During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code.
Your job is to create a program to crack the codes.

On the first line of the input, you will receive the encrypted message.
After that, until the "Decode" command is given, you will be receiving strings with instructions
for different operations that need to be performed upon the concealed message to interpret it and reveal its true content.

There are several types of instructions, split by '|'
    •	"Move {number of letters}":
        o	Moves the first n letters to the back of the string

    •	"Insert {index} {value}":
        o	Inserts the given value before the given index in the string

    •	"ChangeAll {substring} {replacement}":
        o	Changes all occurrences of the given substring with the replacement text
        
        
Input / Constraints:
-------------------
    •	On the first line, you will receive a string with a message.
    •	On the following lines, you will be receiving commands, split by '|' .

Output:
------
    •	After the "Decode" command is received, print this message:
    "The decrypted message is: {message}"


------------ Test Code --------------

Input 1:
-------d
zzHe
ChangeAll|z|l
Insert|2|o
Move|3
Decode


Output 1:
--------
The decrypted message is: Hello


-------------------------------------
"""
