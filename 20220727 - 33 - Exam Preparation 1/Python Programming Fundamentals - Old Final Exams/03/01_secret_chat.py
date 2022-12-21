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
