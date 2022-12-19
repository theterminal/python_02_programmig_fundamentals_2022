# 20220721 - Python Code - String Processing - Exercise
# More Exercise 01 - Extract Person Information - judge url: https://judge.softuni.org/Contests/Practice/Index/1741#0


# ---------------------- version 1 ------------------------ judge: 40%


n = int(input())

for i in range(n):
    name_sub_1, age_sub_1 = input().split('|')
    name_sub_2 = name_sub_1.split('@')

    age_sub_2 = age_sub_1.split('*')
    age_sub_3 = age_sub_2[0].split('#')

    print(f'{name_sub_2[1]} is {age_sub_3[1]} years old.')


# ---------------------- version 2 ------------------------ judge: 40%


n = int(input())
name = ''
age = ''

for i in range(n):
    data_in = input()
    if '@' in data_in and '|' in data_in and '#' in data_in and '*' in data_in:
        name, age = data_in.split('|')
        name_out, name = name.split('@')
        age_out, age = age.split('#')
        age = age.split('*')
        print(f'{name} is {age[0]} years old.')
