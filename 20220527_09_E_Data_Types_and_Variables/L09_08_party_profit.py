# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# 08 - Party Profit - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#7

import math


# --------- version 1 --------------------- judge 100%


group_size = int(input())
days = int(input())
coins_received = 0

if not(1 <= group_size <= 101):
    print(f'Group Size NOT in the specified range')

if not(1 <= days <= 101):
    print(f'Days NOT in the specified range')

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    coins_received += 50
    coins_received -= group_size * 2

    if day % 3 == 0:
        coins_received -= group_size * 3

    if day % 5 == 0:
        coins_received += group_size * 20

        if day % 3 == 0:
            coins_received -= group_size * 2

print(f'{group_size} companions received {math.floor(coins_received / group_size)} coins each.')
