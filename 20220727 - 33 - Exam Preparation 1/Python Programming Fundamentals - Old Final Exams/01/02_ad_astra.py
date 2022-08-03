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


""" -------------------- Ad Astra ----------------------


You are an astronaut who just embarked on a mission across the solar system.
Since you will be in space for a long time, you have packed a lot of food with you.

Create a program, which helps you identify how much food you have left and gives you information about its expiration date.

On the first line of the input, you will be given a text string.
You must extract the information about the food and calculate the total calories. 

First, you must extract the food info.
It will always follow the same pattern rules:
    •	It will be surrounded by "|" or "#" (only one of the two) in the following pattern:

#{item name}#{expiration date}#{calories}#   or 
|{item name}|{expiration date}|{calories}|

    •	The item name will contain only lowercase and uppercase letters and whitespace.

    •	The expiration date will always follow the pattern: "{day}/{month}/{year}",
        where the day, month, and year will be exactly two digits long.

    •	The calories will be an integer between 0-10000

Calculate the total calories of all food items and then determine how many days you can last with the food you have.
Keep in mind that you need 2000kcal a day.


Input / Constraints:
    •	You will receive a single string

Output:
    •	First, print the number of days you will be able to last with the food you have:

"You have food to last you for: {days} days!"

    •	The output for each food item should look like this:
    
"Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"


----------- Test Data -----------


Input 1:
-------
#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|


Output 1:
--------
You have food to last you for: 2 days!
Item: Bread, Best before: 19/03/21, Nutrition: 4000
Item: Apples, Best before: 08/10/20, Nutrition: 200
Item: Carrots, Best before: 06/08/20, Nutrition: 500


---------------------------------


input 2:
-------
$$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|


Output 2:
--------
You have food to last you for: 9 days!
Item: Fish, Best before: 24/12/20, Nutrition: 8500
Item: Ice Cream, Best before: 03/10/21, Nutrition: 9000
Item: Milk, Best before: 05/09/20, Nutrition: 2000


---------------------------------


Input 3:
-------
Hello|#Invalid food#19/03/20#450|$5*(@


Output 3:
--------
You have food to last you for: 0 days!


---------------------------------
"""