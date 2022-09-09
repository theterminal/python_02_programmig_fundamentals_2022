# 20220614 - Python - Functions - Lecture
# 05 - Orders - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#4


# --------------------------- version 1 -------------------------- judge 100%


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


""" ____________ Orders _____________


Write a function that calculates the total price of an order and returns it.
The function should receive one of the following products:

"coffee", "coke", "water", or "snacks",

and a quantity of the product.

The prices for a single piece of each product are: 
•	coffee - 1.50
•	water - 1.00
•	coke - 1.40
•	snacks - 2.00

Print the result formatted to the second decimal place.


___________ Tese Data ______________


Input 1:
-------
water
5


Output 1:
--------
5.00


-----------------------------------


Input 2:
-------
coffee
2


Output 2:
--------
3.00


-----------------------------------
"""

