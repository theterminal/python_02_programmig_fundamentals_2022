# 20220714 - Python - Dictionaries - Exercise
# 06 - Orders - judge url: https://judge.softuni.org/Contests/Compete/Index/1737#5


# ---------------------- version 1 ------------------- judge: 100%


goods = {}

while True:
    data_in = input()
    if data_in == 'buy':
        break

    name, price, quantity = data_in.split(' ')

    if name not in goods:
        goods[name] = {0.00: 0}

    for k, v in goods[name].items():
        goods[name] = {float(price): v + int(quantity)}

for k_1, v_1 in goods.items():
    for k_2, v_2 in v_1.items():
        print(f'{k_1} -> {(k_2 * v_2):.2f}')
