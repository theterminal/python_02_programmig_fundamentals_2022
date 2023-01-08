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
