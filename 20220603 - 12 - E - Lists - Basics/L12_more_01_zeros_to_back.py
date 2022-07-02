# 22020613 - Python Code - L12 - Lists Basics - More Exercise
# 01 - Zeros to Back - judge url: https://judge.softuni.org/Contests/Practice/Index/1726#0


# --------------------- version 1 ---------------------------


lst_nums = [int(i) for i in input().split(', ')]

for i in lst_nums:
    if i == 0:
        lst_nums.remove(0)
        lst_nums.append(0)

print(lst_nums)


# --------------------- version 2 ---------------------------


lst_1 = list(map(int, input().split(', ')))

for i in lst_1:
    if i == 0:
        lst_1.remove(i)
        lst_1.append(0)

print(lst_1)
