# 20220527 - Python - Python Fundamentals - L9 - Data Types and Variables
# 03 - Elevator - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#2

import math


# -------------------- version 1 ----------------------- judge 100%


persons = int(input())
elevator_capacity = int(input())

if elevator_capacity > 0:
    trips = math.ceil(persons / elevator_capacity)
    print(trips)


# -------------------- version 2 ----------------------- judge 100%


persons = int(input())
elevator_capacity = int(input())

trips = 0 if elevator_capacity <= 0 else math.ceil(persons / elevator_capacity)
print(trips)


# -------------------- version 3 ----------------------- judge 100%


persons = int(input())
elevator_capacity = int(input())

if elevator_capacity:
    trips = math.ceil(persons / elevator_capacity)
    print(trips)
