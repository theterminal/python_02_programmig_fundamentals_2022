# 22020613 - Python - L12 - Lists Basics - Exercise
# 09 - Hello France - https://judge.softuni.org/Contests/Compete/Index/1725#8


# _____________________ version 1 _______________________ judge 100%


train_ticket = 150
input_str = input().split('|')             # [0.00:1000.00]
budget_in = float(input())                 # [0.0:1000.0]
budget_left = budget_in

max_price_clothes = 50.00
max_price_shoes = 35.00
max_price_accessories = 20.50

profit = budget_out = 0
lst_new_prices = list()

for i in range(len(input_str)):
    item = input_str[i].split('->')
    price_in = float(item[1])

    if 'Clothes' in item and price_in <= max_price_clothes and budget_left >= price_in:
        budget_left -= price_in
        lst_new_prices.append(f'{(price_in * 1.4):.2f}')
        budget_out += price_in * 1.4

    elif 'Shoes' in item and price_in <= max_price_shoes and budget_left >= price_in:
        budget_left -= price_in
        lst_new_prices.append(f'{(price_in * 1.4):.2f}')
        budget_out += price_in * 1.4

    elif 'Accessories' in item and price_in <= max_price_accessories and budget_left >= price_in:
        budget_left -= price_in
        lst_new_prices.append(f'{(price_in * 1.4):.2f}')
        budget_out += price_in * 1.4

profit = budget_out - budget_in + budget_left
budget_final = budget_in + profit

print(' '.join(lst_new_prices))
print(f'Profit: {profit:.2f}')

if budget_final >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
