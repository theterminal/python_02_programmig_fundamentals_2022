# 20220626 - Python Fundamentals - Mid Exam
# 01 - Burger Bus - judge url: https://judge.softuni.org/Contests/Compete/Index/3477#0


num_cities = int(input())
total_profit = 0

for i in range(1, num_cities + 1):
    city_name = input()
    money_earned = float(input())
    expenses = float(input())

    if (i % 3 == 0) and not(i % 5 == 0):
        expenses *= 1.5

    if i % 5 == 0:
        money_earned *= 0.9

    profit = money_earned - expenses
    print(f'In {city_name} Burger Bus earned {profit:.2f} leva.')
    total_profit += profit

print(f'Burger Bus total profit: {total_profit:.2f} leva.')
