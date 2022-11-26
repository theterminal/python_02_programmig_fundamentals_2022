# 20220523 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 12 - Christmas Spirit - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#11


# ------------------- version 1 -------------------------------- judge: 100%


quantity_of_decorations = int(input())
days_to_christmas = int(input())

price_per_ornament_set,     points_per_ornament_set = 2, 5
price_per_skirt,            points_per_skirt = 5, 3
price_per_garland,          points_per_garland = 3, 10
price_per_lights,           points_per_lights = 15, 17

money_needed = total_spirit = 0

for day in range(1, days_to_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        money_needed += (quantity_of_decorations * price_per_ornament_set)
        total_spirit += points_per_ornament_set

    if day % 3 == 0:
        money_needed += (quantity_of_decorations * (price_per_skirt + price_per_garland))
        total_spirit += (points_per_skirt + points_per_garland)

    if day % 5 == 5 or day % 5 == 0:
        money_needed += (quantity_of_decorations * price_per_lights)
        total_spirit += points_per_lights

        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        money_needed += (price_per_skirt + price_per_garland + price_per_lights)

if days_to_christmas % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {money_needed}')
print(f'Total spirit: {total_spirit}')
