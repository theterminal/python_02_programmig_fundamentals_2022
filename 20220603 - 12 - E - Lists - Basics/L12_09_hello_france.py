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


""" ___________ Hello France ___________


•	You want to go to France by train, and the train ticket costs exactly 150$.
•	You do not have enough money, so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
•	You will receive a collection of items and a budget in the following format:

{type->price|type->price|type->price……|type->price}
{budget}

•	The prices for each of the types cannot exceed a specific price, which is given below:


Type:	        Maximum Price:
----            -------------
Clothes	        50.00
Shoes	        35.00
Accessories	    20.50


•	If a price for a particular item is higher than the maximum price, don't buy it.
•	Every time you buy an item, you have to reduce the budget with its price value.
•	If you don't have enough money for it, you can't buy it.
•	Buy as many items as you can.
•	Next, you should increase the price of each item you have successfully bought by 40% and then sell it.
•	Calculate if the budget after selling all the items is enough for buying the train ticket.


Input / Constraints:
-------------------
•	On the 1st line, you will receive the items with their prices in the format described above – real numbers in the range [0.00……1000.00]
•	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]


Output:
------
•	First, print the list with the bought item’s new prices, formatted to the second decimal point in the following format:

"{price1} {price2} {price3} … {priceN}"

•	Second, print the profit, formatted to the second decimal point in the following format:

"Profit: {profit}"

•	Finally:
    o	If the budget is enough for buying the train ticket, print: "Hello, France!" 
    o	Otherwise, print: "Not enough money."


__________________ Test Data _________________


Input 1:
-------
Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
120


Output 2:
--------
60.62 35.35 51.13
Profit: 42.03
Hello, France!


----------------------------------------------


Input 2:
-------
Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60
90


Output 2:
--------
28.42 21.84 46.62
Profit: 27.68
Not enough money.


----------------------------------------------
"""
