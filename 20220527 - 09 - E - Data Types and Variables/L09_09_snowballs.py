# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# 09 - Snowballs - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#8


# --------- version 1 --------------------- judge 100%


# input information and check of range
num_total_snowballs_made = int(input())

if not(0 <= num_total_snowballs_made <= 100):
    print('Number of show balls entered is OUT of the specified range!')
    quit()

# declaration of variables
weight = time_to_target = quality = value = 0
value_max = weight_value_max = time_to_target_value_max = quality_value_max = 0

# calculations and more inputs
for snowball in range(1, num_total_snowballs_made + 1):
    weight = int(input())
    time_to_target = int(input())
    quality = int(input())

    # range check
    if not (0 <= weight <= 100) or not (1 <= time_to_target <= 500) or not (0 <= quality <= 100):
        print('Some of the data entered is OUT of the specified range!')
        quit()

    value = (weight / time_to_target) ** quality

    if value > value_max:
        value_max = int(value)
        weight_value_max = weight
        time_to_target_value_max = time_to_target
        quality_value_max = quality

print(f'{weight_value_max} : {time_to_target_value_max} = {value_max} ({quality_value_max})')


""" ----------------- Snowballs -------------------


Tony and Andi love playing in the snow and having snowball fights, but they always argue about who makes the best snowballs.
They have decided to involve you in their fray by writing a program that calculates snowball data and outputs the best snowball value.
You will receive 'N' – an integer, the number of snowballs being made by Tony and Andi.

On the following lines, you will receive 3 inputs for each snowball:
    •	The weight of the snowball (integer).
    •	The time needed for the snowball to get to its target (integer).
    •	The quality of the snowball (integer).

For each snowball, you must calculate its value by the following formula:

(snowball_weight / snowball_time) ** snowball_quality

In the end, you must print the highest calculated value of a snowball.

Input:
-----
    •	On the first input line, you will receive N – the number of snowballs.
    •	On the next N*3 input lines, you will be receiving data about each snowball.

Output:
------
    •	You need to print the highest calculated snowball's value in the format: 
    "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"

Constraints:
-----------
    •	The number of snowballs (N) will be an integer in range [0, 100].
    •	The weight is an integer in the range [0, 1000].
    •	The time is an integer in the range [1, 500].
    •	The quality is an integer in the range [0, 100].


--------------- Test Data ----------------


Input 1:
-------
2
10
2
3
5
5
5


Output 1:
--------
10 : 2 = 125 (3)


------------------------------------------


Input 2:
-------
3
10
5
7
16
4
2
20
2
2


Output 2:
--------
10 : 5 = 128 (7)


-------------------------------------------

"""
