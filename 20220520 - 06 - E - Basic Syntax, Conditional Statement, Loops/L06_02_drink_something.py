# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 02 - Drink Something - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#1


# ------------- version 1 ----------------------- judge: 100%


persons_age_entered = int(input())

if persons_age_entered <= 14:
    print('drink toddy')
elif persons_age_entered <= 18:
    print('drink coke')
elif persons_age_entered <= 21:
    print('drink beer')
elif persons_age_entered > 21:
    print('drink whisky')


""" ---------------- Drink Something -------------------


•	Kids drink toddy
•	Teens drink coke
•	Young adults drink beer
•	Adults drink whisky

Create a program that receives a person's age and prints what he/she drinks.

Rules:
•	A kid is defined as someone under or at the age of 14.
•	A teen is defined as someone under or at the age of 18.
•	A young adult is defined as someone under or at the age of 21.
•	An adult is defined as someone above the age of 21.

Note: All the values are inclusive except the last one!


--------- Test Data -----------------


Input 1:                Output 1:
-------                 --------
13                      drink toddy


-------------------------------------


Input 2:                Output 2:
-------                 --------
17                      drink coke


-------------------------------------


Input 3:                Output 3:
-------                 --------
21	                    drink beer


-------------------------------------


Input 4:                Output 4:
-------                 --------
30	                    drink whisky


"""
