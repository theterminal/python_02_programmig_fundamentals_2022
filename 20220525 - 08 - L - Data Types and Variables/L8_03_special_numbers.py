# 20220529 - Python - Python Fundamentals - L9 - Data Types and Variables
# 03 - Special Numbers - judge url: https://judge.softuni.org/Contests/Practice/Index/1721#2

# --- version 1 --- Working with strings ---

num_entered = int(input())

for num in range(1, num_entered + 1):
    sum_digits = 0
    str_num = str(num)

    for j in range(len(str_num)):
        num_to_sum = int(str_num[j])
        sum_digits += num_to_sum

    if (sum_digits == 5) or (sum_digits == 7) or (sum_digits == 11):
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')

# --- version 2 --- Working with numbers only ---

num_entered = int(input())

for num in range(1, num_entered + 1):
    sum_digits = 0
    work_num = num

    while work_num > 0:
        sum_digits += work_num % 10
        work_num = int(work_num / 10)

    if (sum_digits == 5) or (sum_digits == 7) or (sum_digits == 11):
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
