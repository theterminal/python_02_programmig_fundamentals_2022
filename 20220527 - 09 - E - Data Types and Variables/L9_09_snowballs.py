# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# 09 - Snowballs - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#8

num_total_snowballs_made = int(input())
weight = time_to_target = quality = value = 0
value_max = weight_value_max = time_to_target_value_max = quality_value_max = 0

if not(0 <= num_total_snowballs_made <= 100):
    print('Number of show balls entered is OUT of the specified range!')
    quit()

for snowball in range(1, num_total_snowballs_made + 1):
    weight = int(input())
    time_to_target = int(input())
    quality = int(input())

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
