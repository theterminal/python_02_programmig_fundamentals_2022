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
