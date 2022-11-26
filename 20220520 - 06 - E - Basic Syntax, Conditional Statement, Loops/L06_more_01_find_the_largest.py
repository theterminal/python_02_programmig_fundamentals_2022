# 20220525 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# More Exercise 01 - Find The Largest - judge url: https://judge.softuni.org/Contests/Practice/Index/1720#0


# ----------------------- version 2 --- using list comprehension ------------ judge: 100%


print(''.join([str(i) for i in sorted((int(i) for i in input()), reverse=True)]))


# ----------------------- version 1 ------------------------------------------ judge: 100%


num_entered = input()
max_num = 0
count_index = 0
new_str_num = ''

for _ in range(len(num_entered)):

    for i in range(len(num_entered)):
        int_num = int(num_entered[i])

        if int_num > max_num:
            max_num = int_num
            count_index = i

    new_str_num += str(max_num)
    max_num = 0
    num_entered = num_entered[:count_index] + num_entered[count_index + 1:]

print(new_str_num)
