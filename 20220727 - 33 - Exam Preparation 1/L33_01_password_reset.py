# 20220727 - Python - Exam Preparation 1
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
