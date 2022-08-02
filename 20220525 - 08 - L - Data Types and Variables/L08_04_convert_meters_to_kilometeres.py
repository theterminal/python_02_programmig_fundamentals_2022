# 20220529 - Python - Python Fundamentals - L08 - Data Types and Variables
# 04 - Convert Meters to Kilometres - judge url: https://judge.softuni.org/Contests/Practice/Index/1721#3


# ------------- version 1 ----------------------- judge: 100%


distance_meters = int(input())
distance_kilometers = distance_meters / 1000

print(f'{distance_kilometers:.2f}')


""" ----------------- Convert Meters to Kilometres ------------------


You will be given an integer that represents a distance in meters.
Write a program that converts meters to kilometers formatted to the second decimal point.


--------- Test Data ----------


Input 1:
-------
1852


Output 1:
--------
1.85


------------------------------


Input 2:
-------
798


Output 2:
--------
0.80


"""
