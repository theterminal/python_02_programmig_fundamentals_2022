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


""" -------------------- Elevator -------------------------


Calculate how many courses will be needed to elevate 'N' persons by using an elevator with a capacity of 'P' persons.
The input holds two lines: the number of people 'N' and the capacity 'P' of the elevator.


------------------- Test Data -----------------------


Input 1:
-------
17
3


Output 1:
--------
6


Comments: 5 courses * 3 people + 1 course * 2 persons


------------------------------------------------------


Input 2:
-------
4
5


Output 2:
--------
1


Comments: All the persons fit inside the elevator. Only one course is needed.


-----------------------------------------------------


Input 3:
-------
10
5


Output 3:
--------
2


Comments:   2 courses * 5 people

"""
