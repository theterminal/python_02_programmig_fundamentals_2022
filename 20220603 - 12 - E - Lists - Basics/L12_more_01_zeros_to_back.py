# 22020613 - Python Code - L12 - Lists Basics - More Exercise
# 01 - Zeros to Back - judge url: https://judge.softuni.org/Contests/Practice/Index/1726#0

str_in = input().split(', ')
lst_num_from_str_in = [int(i) for i in str_in]

for i in lst_num_from_str_in:
    if i == 0:
        lst_num_from_str_in.remove(0)
        lst_num_from_str_in.append(0)

print(lst_num_from_str_in)
