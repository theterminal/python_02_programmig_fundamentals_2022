# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# 10 - Gladiator Expenses - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#9


# --------- version 1 --------------------- judge 100%


while True:
    lost_fights = int(input())
    if 0 <= lost_fights <= 1000:
        break

    print('The \'lost fights\' data is OUT of range!')

while True:
    price_helmet = float(input())
    if 0 <= price_helmet <= 1000:
        break

    print('The \'helmet price\' data is OUT of range!')

while True:
    price_sword = float(input())
    if 0 <= price_sword <= 1000:
        break

    print('The \'sword price\' data is OUT of range!')

while True:
    price_shield = float(input())
    if 0 <= price_shield <= 1000:
        break

    print('The \'shield price\' data is OUT of range!')

while True:
    price_armor = float(input())
    if 0 <= price_armor <= 1000:
        break
    print('The \'armor price\' data is OUT of range!')

total_expenses = 0
counter_broken_shield = 0

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


""" ---------------- Gladiator Expences ------------------


As a gladiator, Peter needs to repair his broken equipment when he loses a fight.
His equipment consists of a helmet, a sword, a shield, and an armor. 
    •	You will receive Peter's lost fights count.
    •	Every second lost game, his helmet is broken.
    •	Every third lost game, his sword is broken.
    •	When both his sword and helmet are broken in the same lost fight, his shield also breaks.
    •	Every second time his shield brakes, his armor also needs to be repaired.
    •	You will receive the price of each item in his equipment.

Calculate his expenses for the year for renewing his equipment.

Input / Constraints:
-------------------
The input will consist of 5 lines:
    •	On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
    •	On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000]. 
    •	On the third line, you will receive the sword price - a floating-point number in the range [0, 1000]. 
    •	On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000]. 
    •	On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].

Output:
------
    •	As output, you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"


------------------ Test Data ------------------


Input 1:
-------
7
2
3
4
5


Output 1:
--------
Gladiator expenses: 16.00 aureus


-----------------------------------------------


Input 2:
-------
23
12.50
21.50
40
200


Output 2:
--------
Gladiator expenses: 608.00 aureus


-----------------------------------------------

"""
