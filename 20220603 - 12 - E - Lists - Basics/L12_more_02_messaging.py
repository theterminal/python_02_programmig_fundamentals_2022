# 22020613 - Python Code - L12 - Lists Basics - More Exercise
# 02 - Messaging - judge url: https://judge.softuni.org/Contests/Practice/Index/1726#1

str_1 = input().split()
str_2 = input()

sum_nums = sum_sub = index_model = 0

# code for the digits part
for i in range(len(str_1)):
    for j in range(len(str_1[i])):
        num = int(str_1[i][j])
        sum_sub += num
    index_model += sum_sub
    sum_sub = 0
print(index_model, '- index model')

# code for the string part
lst_from_str_2 = list()
count_char = len(str_2)
print(count_char, '- counter_char')

for j in str_2:
    lst_from_str_2.append(j)

print(lst_from_str_2)

message = list()
index_to_print = 0
index_match = 0
flag = False
out = 0

while len(lst_from_str_2) > 0:
    while True:
        if index_match == index_model:
            break
        else:
            index_match += 1

        index_to_print += 1
        if index_to_print == len(lst_from_str_2):
            index_to_print = 0

    message.append(lst_from_str_2[index_to_print])
    lst_from_str_2.pop(index_to_print)
    index_match = 0
    index_to_print = 0

print(message)

