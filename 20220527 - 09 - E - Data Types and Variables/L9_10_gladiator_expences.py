# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# 10 - Gladiator Expenses - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#9

lost_fights = int(input())
if not(0 <= lost_fights <= 1000):
    print('The \'lost fights\' data is OUT of range!')
    quit()

price_helmet = float(input())
if not(0 <= price_helmet <= 1000):
    print('The \'helmet price\' data is OUT of range!')
    quit()

price_sword = float(input())
if not(0 <= price_sword <= 1000):
    print('The \'sword price\' data is OUT of range!')
    quit()

price_shield = float(input())
if not(0 <= price_shield <= 1000):
    print('The \'shield price\' data is OUT of range!')
    quit()

price_armor = float(input())
if not(0 <= price_armor <= 1000):
    print('The \'armor price\' data is OUT of range!')
    quit()

total_expenses, counter_broken_shield = 0, 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        total_expenses += price_helmet

    if fight % 3 == 0:
        total_expenses += price_sword

        if fight % 2 == 0:
            total_expenses += price_shield
            counter_broken_shield += 1
            if counter_broken_shield == 2:
                total_expenses += price_armor
                counter_broken_shield = 0

print(f'Gladiator expenses: {total_expenses:.2f} aureus')