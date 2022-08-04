# 20220523 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 11 - Easter Bread - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#10


# ------------------- version 1 -------------------------------- judge: 100%


budget = float(input())
price_flour_per_kg = float(input())
price_1_pack_eggs = price_flour_per_kg * 0.75
price_1l_milk = price_flour_per_kg * 1.25
price_025l_milk = (price_flour_per_kg * 1.25) / 4

flour_kgs_in_stock = num_egg_packs_in_stock = milk_l_in_stock = 0
count_bread_made = count_bread_temp = 0
total_colored_eggs = counter_colored_eggs = 0

while True:
    if num_egg_packs_in_stock == 0:
        if budget >= price_1_pack_eggs:
            num_egg_packs_in_stock += 1
            budget -= price_1_pack_eggs
        else:
            break

    if flour_kgs_in_stock == 0:
        if budget >= price_flour_per_kg:
            flour_kgs_in_stock += 1
            budget -= price_flour_per_kg
        else:
            break

    if milk_l_in_stock == 0:
        if budget >= price_025l_milk:
            milk_l_in_stock += 0.25
            budget -= price_025l_milk
        else:
            break

    while True:
        if num_egg_packs_in_stock >= 1 and flour_kgs_in_stock >= 1 and milk_l_in_stock >= 0.25:
            count_bread_made += 1
            num_egg_packs_in_stock -= 1
            flour_kgs_in_stock -= 1
            milk_l_in_stock -= 0.25
            total_colored_eggs += 3
            count_bread_temp += 1

            if count_bread_temp == 3:
                total_colored_eggs -= (count_bread_made - 2)
                count_bread_temp = 0
        else:
            break

budget = budget \
         + (num_egg_packs_in_stock * price_1_pack_eggs) \
         + (flour_kgs_in_stock * price_flour_per_kg) \
         + (milk_l_in_stock * price_1l_milk)

print(f'You made {count_bread_made} loaves of Easter bread! Now you have {total_colored_eggs} eggs and {budget:.2f}BGN left.')


""" -------------------- Easter Bread -----------------------


Since it is Easter, you have decided to make some loaves of Easter bread and exchange them for eggs.

Create a program that calculates how many loaves you can make with the budget you have.

First, you will receive your budget.
Then, you will receive the price for 1 kg flour.

Here is the recipe for one loaf:
    •   Eggs	1 pack
    •   Flour	1 kg
    •   Milk	0.250 l

The price for 1 pack of eggs is 75% of the price for 1 kg flour.
The price for 1l milk is 25% more than the price for 1 kg flour.
Notice that you need 0.250l milk for one loaf of bread, and the calculated price is for 1l.

Start cooking the loaves and keep making them until you have enough budget.

Keep in mind that:
    •	For every loaf of bread that you make, you will receive 3 colored eggs.

    •	For every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3 colored eggs for your bread.
        The count of eggs you will lose is calculated when you subtract 2 from your current count of loaves - ({current_bread_count} - 2)

In the end, print the loaves of bread you made, the eggs you have collected, and the money you have left, formatted to the 2nd decimal place, in the following format:
"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."


Input / Constraints:
--------------------
    •	On the 1st line, you will receive the budget - a real number in the range [0.0…100000.0]
    •	On the 2nd line, you will receive the price for 1 kg flour - a real number in the range [0.0…100000.0]
    •	The input will always be in the correct format
    •	You will always have a remaining budget
    •	There will not be a case in which the eggs become a negative count

Output:
------
    •	In the end, print the number of loaves of Easter bread you have made, the colored eggs you have gathered, and the money formatted to the 2nd decimal place in the format described above.


--------------- Test Data ---------------


Input 1:
-------
20.50
1.25


Output 1:
--------
You made 7 loaves of Easter bread! Now you have 16 eggs and 2.45BGN left


-----------------------------------------


Input 2:
-------
15.75
1.4


Output 2:
--------
You made 5 loaves of Easter bread! Now you have 14 eggs and 1.31BGN left.


"""