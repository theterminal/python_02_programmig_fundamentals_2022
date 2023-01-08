# 20220626 - Python Fundamentals - Mid Exam
# 02 - Space Travel - judge url: https://judge.softuni.org/Contests/Compete/Index/3477#1


# ---------------- version 1 --------------------- judge 100%


travel_route = input().split('||')
fuel = int(input())
ammo = int(input())

for i in travel_route:
    if i == 'Titan':
        print(f'You have reached Titan, all passengers are safe.')
        break

    command = i.split(' ')

    if command[0] == 'Travel':
        if fuel >= int(command[1]):
            print(f'The spaceship travelled {int(command[1])} light-years.')
            fuel -= int(command[1])
        else:
            print('Mission failed.')
            break

    elif command[0] == 'Enemy':
        if ammo >= int(command[1]):
            print(f'An enemy with {int(command[1])} armour is defeated.')
            ammo -= int(command[1])
        else:
            if fuel >= (int(command[1]) * 2):
                print(f'An enemy with {int(command[1])} armour is outmaneuvered.')
                fuel -= (int(command[1]) * 2)
            else:
                print('Mission failed.')
                break

    elif command[0] == 'Repair':
        print(f'Ammunitions added: {int(command[1]) * 2}.')
        print(f'Fuel added: {int(command[1])}.')
        ammo += (int(command[1]) * 2)
        fuel += int(command[1])
