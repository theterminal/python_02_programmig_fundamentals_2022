# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 05 - Orders - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#4


# ------------- version 1 ----------------------- judge: 100%


num_of_orders = int(input())
total_price = 0

for i in range(num_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not(0.01 <= price_per_capsule <= 100.00):
        continue
    elif not(1 <= days <= 31):
        continue
    elif not(1 <= capsules_per_day <= 2000):
        continue

    coffee_price = price_per_capsule * days * capsules_per_day
    print(f'The price for the coffee is: ${coffee_price:.2f}')
    total_price += coffee_price

print(f'Total: ${total_price:.2f}')
