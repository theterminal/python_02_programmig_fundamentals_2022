# 20220621 - Python Code - Mid Exam Preparation
# 04 - Moving Target - judge url: https://judge.softuni.org/Contests/Practice/Index/2305#2


def func_shoot(index, value, targets):
    if 0 <= index < len(targets):
        if targets[index] - value <= 0:
            targets.pop(index)
        else:
            targets[index] -= value
    return targets


def func_add(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print('Invalid placement!')
    return targets


def func_strike(index, value, targets):
    index_validator = 0 <= index - value and index + value < len(targets)
    if index_validator:
        target_start_index = index - value
        target_end_index = index + value
        targets = [targets[i] for i in range(len(targets)) if i < target_start_index or i > target_end_index]
    else:
        print('Strike missed!')
    return targets


def func_main(targets):
    while True:
        command = input()

        if command == 'End':
            print('|'.join(str(i) for i in targets))
            break

        command = command.split(' ')
        action = command[0]
        index = int(command[1])
        value = int(command[2])

        if action == 'Shoot':
            targets = func_shoot(index, value, targets)
        elif action == 'Add':
            targets = func_add(index, value, targets)
        elif action == 'Strike':
            targets = func_strike(index, value, targets)


targets_in = list(map(int, input().split()))                            # int [1 : 10_000]
func_main(targets_in)
