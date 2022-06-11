# 20220527 - Python - Python Fundamentals - L9 - Data Types and Variables
# 07 - Water Overflow - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#6

num_lines = range(int(input()))
tank_capacity_l = 255
in_tank_l = 0

for _ in num_lines:
    l_to_pour_in_tank = float(input())

    if (tank_capacity_l - l_to_pour_in_tank) < 0:
        print('Insufficient capacity!')
        continue

    tank_capacity_l -= l_to_pour_in_tank
    in_tank_l += l_to_pour_in_tank

print(int(in_tank_l))
