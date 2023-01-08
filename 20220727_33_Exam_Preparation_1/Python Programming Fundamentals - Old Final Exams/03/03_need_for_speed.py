# 20220729 - Python Code - Exam Preparation 2
# 03 - Need For Speed - judge url: https://judge.softuni.org/Contests/Practice/Index/2307#2


# ------------------------- version 1 ------------------------ judge: 100%


num_cars = int(input())
dict_cars = {}
make = ''

for i in range(num_cars):
    data = input()
    make, millage, fuel = data.split('|')
    dict_cars[make] = [int(millage), int(fuel)]

while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split(' : ')
    action = command[0]
    car = command[1]

    if action == 'Drive':
        distance = int(command[2])
        fuel_needed = int(command[3])

        if dict_cars[car][1] < fuel_needed:
            print('Not enough fuel to make that ride')
        else:
            dict_cars[car][0] = dict_cars[car][0] + distance
            dict_cars[car][1] = dict_cars[car][1] - fuel_needed
            print(f'{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.')

        if dict_cars[car][0] >= 100_000:
            print(f'Time to sell the {car}!')
            dict_cars.pop(car)

    elif action == 'Refuel':
        fuel = int(command[2])

        if dict_cars[car][1] + fuel > 75:
            print(f'{car} refueled with {75 - dict_cars[car][1]} liters')
            dict_cars[car][1] = 75
        else:
            dict_cars[car][1] += fuel
            print(f'{car} refueled with {fuel} liters')

    elif action == 'Revert':
        kilometers = int(command[2])

        dict_cars[car][0] -= kilometers
        if not (dict_cars[car][0] <= 10_000):
            print(f'{car} mileage decreased by {kilometers} kilometers')
        else:
            dict_cars[car][0] = 10_000

for k, v in dict_cars.items():
    print(f'{k} -> Mileage: {v[0]} kms, Fuel in the tank: {v[1]} lt.')
