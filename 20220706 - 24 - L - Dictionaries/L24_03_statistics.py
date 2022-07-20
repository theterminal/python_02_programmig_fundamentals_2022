# 20220706 - Python Code - Dictionaries - Lecture
# 03 - Statistics - judge url: https://judge.softuni.org/Contests/Practice/Index/1736#2


# --------------------- version 1 --------------------------- judge 100%


products = {}

while True:
    command = input()
    if command == 'statistics':
        break

    token = command.split(': ')
    product = token[0]
    quantity = int(token[1])

    if product not in products:
        products[product] = 0
    products[product] += quantity

print(f'Products in stock:')

for product, quantity in products.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {len(products.keys())}\nTotal Quantity: {sum(products.values())}')
