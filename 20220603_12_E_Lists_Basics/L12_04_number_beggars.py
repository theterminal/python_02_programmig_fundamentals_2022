# 20220603 - Python - L12 - Lists Basics - Exercise
# 04 - Number Beggars - judge url: https://judge.softuni.org/Contests/Compete/Index/1725#3


# ---------------------- version 1 --------------------------------- judge 100%


lst_nums = list(map(int, input().split(', ')))
num_beggars = int(input())

lst_out = []

for beggar in range(num_beggars):
    sum_current_beggar = 0

    for num in range(beggar, len(lst_nums), num_beggars):
        sum_current_beggar += lst_nums[num]

    lst_out.append(sum_current_beggar)

print(lst_out)


# ---------------------- version 2 --------------------------------- judge 100%


lst_collect = list(map(int, input().split(', ')))
num_collectors = int(input())

lst_collector_final = []

for collector in range(num_collectors):
    middle_list = lst_collect[collector::num_collectors]
    lst_collector_final.append(sum(middle_list))

print(lst_collector_final)
