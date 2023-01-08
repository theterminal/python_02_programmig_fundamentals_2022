# 20220729 - Python Code - Exam Preparation 2
# 01 - Activation Keys - judge url: https://judge.softuni.org/Contests/Practice/Index/2302#0


# ------------------------- version 1 ------------------------ judge: 100%


key = input()

while True:
    data_in = input()
    if data_in == 'Generate':
        break

    command = data_in.split('>>>')

    if command[0] == 'Contains':

        if command[1] in key:
            print(f'{key} contains {command[1]}')
        else:
            print('Substring not found!')

    elif command[0] == 'Flip':

        if command[1] == 'Upper':
            key = key[:int(command[2])] + key[int(command[2]): int(command[3])].upper() + key[int(command[3]):]
            print(key)

        elif command[1] == 'Lower':
            key = key[:int(command[2])] + key[int(command[2]): int(command[3])].lower() + key[int(command[3]):]
            print(key)

    elif command[0] == 'Slice':
        key = key[: int(command[1])] + key[int(command[2]):]
        print(key)

print(f'Your activation key is: {key}')
