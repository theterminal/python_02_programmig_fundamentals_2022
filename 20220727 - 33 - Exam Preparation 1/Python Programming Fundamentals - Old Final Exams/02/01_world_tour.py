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
