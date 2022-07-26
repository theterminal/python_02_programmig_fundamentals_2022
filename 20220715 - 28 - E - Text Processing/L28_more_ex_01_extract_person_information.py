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


""" ------------ Extract Person Information -----------------------


Write a program that reads 'N' lines of strings and extracts the name and the age of a given person:

•	The person's name will be surrounded by "@" and "|" in the format "@{name}|".
•	The person's age will be surrounded by "#" and "*" in the format "#{age}*".

Example:
"Hello my name is @Peter| and I am #20* years old." 

For each found name-age pair, print a line in the following format:
"{name} is {age} years old."


---------------------------------------------------


Input 1:
--------
2
Here is a name @George| and an age #18*
Another name @Billy| #35* is his age


Output 1:
---------
George is 18 years old.
Billy is 35 years old.


---------------------------------------------------


Input 2:
--------
3
random name @lilly| random digits #5*age
@Marry| with age #19*
here Comes @Garry|he is #48* years old


Output 2:
--------
lilly is 5 years old.
Marry is 19 years old.
Garry is 48 years old.


---------------------------------------------------

"""