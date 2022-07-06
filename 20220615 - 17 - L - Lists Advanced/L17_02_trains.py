# 20220616 - Python Code - Lists Advance - Lecture
# 02 - Trains - judge: https://judge.softuni.org/Contests/Practice/Index/1730#1


wagons = int(input())
train = [0 for n in range(wagons)]                      # train = [0] * wagons

while True:
    command = input()
    if command == 'End':
        break

    lst_com = [n for n in command.split(' ')]
    operation = lst_com[0]

    if operation == 'add':
        num_people = int(lst_com[1])
        train[-1] += num_people
    else:
        index = int(lst_com[1])
        people = int(lst_com[2])

        if operation == 'insert':
            train[index] += people

        elif operation == 'leave':
            train[index] -= people

print(train)
