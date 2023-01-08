# 20220701 - Python - Objects and Classes - Exercise
# 08 - Vehicle - judge url: https://judge.softuni.org/Contests/Compete/Index/1734#7


# ------------------------- version 1 ---------------------------- judge 100%


class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            change = money - self.price
            self.owner = owner
            return f'Successfully bought a {self.type}. Change: {change:.2f}'
        elif money < self.price:
            return f'Sorry, not enough money'
        elif self.owner is not None:
            return f'Car already sold'

    def sell(self):
        if self.owner is not None:
            self.owner = None
        return f'Vehicle has no owner'

    def __repr__(self):
        if self.owner is not None:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        return f'{self.model} {self.type} is on sale: {self.price}'


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
