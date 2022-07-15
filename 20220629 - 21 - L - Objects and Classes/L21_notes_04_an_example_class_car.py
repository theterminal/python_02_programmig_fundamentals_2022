# 20220629 - Python Code - Objects and Classes - Lecture
# Notes 04


class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def show_info(self):
        return f'A car has: year = {self.year}, make = {self.make} and model = {self.model}...'

    def make_a_beep(self):
        return f'BEEP!!! from {self.make} and {self.model}'


cars_data = []

while True:
    command = input()
    if command == 'End':
        break
    command_year, command_make, command_model = command.split(', ')
    car = Car(command_year, command_make, command_model)
    cars_data.append(car)

print(f'total cars entered = {len(cars_data)}')

for car in cars_data:
    print(f'\nYear: {car.year}\nMake: {car.make}\nModel: {car.model}\n')

print(f'Car is: {cars_data[2].make_a_beep()}')


# --------------------------------
# use the following input

"""

2001, 'Peugeot', '306 2.0 HDI'
1981, 'Jeep', '16 HDI'
1969, 'Жигули', '65 конски сили'
1989, 'Лада Нива', '1500 S'
2003, 'Cadillac', 'Escalade EXT'
End

"""

