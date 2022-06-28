# 20220523 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 11 - Easter Bread - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#10


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
