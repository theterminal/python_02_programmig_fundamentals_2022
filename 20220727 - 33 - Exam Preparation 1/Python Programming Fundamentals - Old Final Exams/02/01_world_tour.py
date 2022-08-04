# 20220730 - Python Code - Exam Preparation
# 01 - World Tour - judge url: https://judge.softuni.org/Contests/Practice/Index/2518#0


# ------------------------- version 1 ------------------------ judge: 100%


data = input()

while True:
    command = input()
    if command == 'Travel':
        break

    command = command.split(':')
    action = command[0]

    if action == 'Add Stop':
        index = int(command[1])
        string = command[2]

        if 0 <= index < len(data):
            data = data[:index] + string + data[index:]

    elif action == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])

        if (0 <= start_index < len(data)) and (0 <= end_index < len(data)):
            data = data[:start_index] + data[end_index + 1:]

    elif action == 'Switch':
        old_string = command[1]
        new_string = command[2]

        data = data.replace(old_string, new_string)
    
    print(data)

print(f'Ready for world tour! Planned stops: {data}')


""" ------------------- World Tour ----------------------


You are a world traveler, and your next goal is to make a world tour.
To do that, you have to plan out everything first.
To start with, you would like to plan out all of your stops where you will have a break.

On the first line, you will be given a string containing all of your stops.
Until you receive the command "Travel", you will be given some commands to manipulate that initial string.

The commands can be:
    •	"Add Stop:{index}:{string}":
        o	Insert the given string at that index only if the index is valid

    •	"Remove Stop:{start_index}:{end_index}":
        o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid

    •	"Switch:{old_string}:{new_string}":
        o	If the old string is in the initial string, replace it with the new one (all occurrences)

Note: After each command, print the current state of the string if it is valid!

After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"

Input / Constraints:
-------------------
    •	JavaScript: you will receive a list of strings
    •	An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.

Output:
------
    •	Print the proper output messages in the proper cases as described in the problem description
    
    
----------------- Test Data -----------------------


Input 1:
-------
Hawai::Cyprys-Greece
Add Stop:7:Rome
Remove Stop:11:16
Switch:Hawai:Bulgaria
Travel


Output 1:
--------
Hawai::RomeCyprys-Greece
Hawai::Rome-Greece
Bulgaria::Rome-Greece
Ready for world tour! Planned stops: Bulgaria::Rome-Greece


---------------------------------------------------

"""
