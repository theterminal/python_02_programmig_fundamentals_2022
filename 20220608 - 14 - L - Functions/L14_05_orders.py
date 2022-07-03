# 20220614 - Python Code - Functions - Lecture
# 05 - Orders - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#4


def orders(product: str, quantity: int):
    price = 0

    if product == 'coffee':
        price = 1.50
    elif product == 'water':
        price = 1.00
    elif product == 'coke':
        price = 1.40
    elif product == 'snacks':
        price = 2.00

    return f'{(price * quantity):.2f}'


prod = input()
q = int(input())
print(orders(prod, q))

