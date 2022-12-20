# 20220802 - Python Code - Exam Preparation
# 02 - Ad Astra - judge url: https://judge.softuni.org/Contests/Practice/Index/2525#1

import re


# ------------------------- version 1 ------------------------ judge: 100%


pattern_food = r'\#[A-za-z\s]+\#\d{2}\/\d{2}\/\d{2}\#\d{1,5}\#|\|[A-za-z\s]+\|\d{2}\/\d{2}\/\d{2}\|\d{1,5}\|'
data = input()

result = re.findall(pattern_food, data)
output = {}
total_cal = 0
text_out = ''

for food in result:
    divider = food[0]

    name = food.split(divider)
    food_name = name[1]
    exp_date = name[2]
    cal = name[3]
    total_cal += int(cal)

    text_out += f'Item: {food_name}, Best before: {exp_date}, Nutrition: {cal}\n'

print(f'You have food to last you for: {total_cal // 2000} days!')
print(text_out)


# ------------------------- version 2 ------------------------ judge: 100%


def incoming_data():
    data = input()

    return data


def pattern_result(data, text_out, total_cal):
    pattern_food = r'\#[A-za-z\s]+\#\d{2}\/\d{2}\/\d{2}\#\d{1,5}\#|\|[A-za-z\s]+\|\d{2}\/\d{2}\/\d{2}\|\d{1,5}\|'
    result = re.findall(pattern_food, data)

    total_cal = 0
    text_out = ''

    for food in result:
        divider = food[0]
        name = food.split(divider)
        food_name = name[1]
        exp_date = name[2]
        cal = name[3]
        total_cal += int(cal)
        text_out += f'Item: {food_name}, Best before: {exp_date}, Nutrition: {cal}\n'

    return text_out, total_cal


def output(text_out, total_cal):
    print(f'You have food to last you for: {total_cal // 2000} days!')
    print(text_out)


def ad_astra():
    data_entered = incoming_data()
    text_out, total_cal = pattern_result(data_entered, text_out=None, total_cal=None)
    output(text_out, total_cal)


ad_astra()
