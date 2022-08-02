# 20220529 - Python - Python Fundamentals - L08 - Data Types and Variables
# 02 - Centuries to Minutes - judge url: https://judge.softuni.org/Contests/Practice/Index/1721#1


# ------------- version 2 ----------------------- judge: 100%


from decimal import Decimal

centuries_entered = int(input())

years = centuries_entered * 100
days = int(years * Decimal(365.2422))
hours = days * 24
minutes = hours * 60

print(f'{centuries_entered} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')


# ------------- version 1 ----------------------- judge: 100%


centuries_entered = int(input())

years = centuries_entered * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{centuries_entered} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')


""" ---------------------- Centuries To Minutes ------------------------


Write a program that reads an integer number of centuries and converts it to years, days, hours, and minutes.


------- Test Data ----------


Input 1:
-------
1


Output 1:
--------
1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes


----------------------------


Input 2:
-------
5


Output 2:
--------
5 centuries = 500 years = 182621 days = 4382904 hours = 262974240 minutes


"""
