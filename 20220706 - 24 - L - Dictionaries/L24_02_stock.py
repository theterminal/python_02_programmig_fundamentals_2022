# 20220706 - Python Code - Dictionaries - Lecture
# 02 - Stock - judge url: https://judge.softuni.org/Contests/Practice/Index/1736#1


# --------------------- version 3 --------------------------- judge 100%


data_in = input().split(' ')
products_to_search_for = input().split(' ')

dict_data_in = {data_in[i]: int(data_in[i + 1]) for i in range(0, len(data_in), 2)}

for product in products_to_search_for:
    if product in dict_data_in:
        print(f'We have {dict_data_in[product]} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')


# --------------------- version 2 --------------------------- judge 100%


data_in = input().split(' ')
products_to_search_for = input().split(' ')

dict_data_in = {}

for i in range(0, len(data_in), 2):
    dict_data_in[data_in[i]] = int(data_in[i + 1])

for product in products_to_search_for:
    if product in dict_data_in:
        print(f'We have {dict_data_in[product]} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')


# --------------------- version 1 --------------------------- judge 100%


items_in_stock = input().split(' ')
items = {}

for i in range(0, len(items_in_stock), 2):
    key = items_in_stock[i]
    value = items_in_stock[i + 1]
    items[key] = int(value)

searched_products = input().split(' ')

for product in searched_products:
    if product in items:
        print(f"We have {items[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
