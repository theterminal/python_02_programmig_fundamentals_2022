# 20220603 - Python Code - L12 - Lists Basics - Exercise
# 04 - Number Beggars - judge url: https://judge.softuni.org/Contests/Compete/Index/1725#3

list_str_entered = input().split(', ')
num_beggars = int(input())

list_sums_print = []
current_beggar = 0

# list_int = [int(i) for i in list_str]

list_int = []

for element in list_str_entered:
    list_int.append(int(element))

while current_beggar < num_beggars:
    sum_current_beggar = 0

    for current_index in range(current_beggar, len(list_int), num_beggars):
        sum_current_beggar += list_int[current_index]

    current_beggar += 1
    list_sums_print.append(sum_current_beggar)

print(list_sums_print)

# ----------- someone else ----------------

list_money = input().split(", ")
num_beggars = int(input())

list_sums_current_beggar = []
list_totals_all_beggars = []

for current_beggar in range(num_beggars):

    for index in range(current_beggar, len(list_money), num_beggars):
        list_sums_current_beggar.append(int(list_money[index]))

    list_totals_all_beggars.append(sum(list_sums_current_beggar))
    list_sums_current_beggar.clear()

print(list_totals_all_beggars)


# ----------- someone else ----------------

collect = input()
collectors = int(input())

collect_list = list(map(int, collect.split(", ")))
collector_final = []

for i in range(collectors):
    middle_list = collect_list[i::collectors]
    collector_final.append(sum(middle_list))

print(collector_final)
