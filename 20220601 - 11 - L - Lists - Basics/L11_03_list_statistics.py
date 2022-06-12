# 20220601 - Python Code - L11 - Lists-Basics
# 03 - List Statistics - judge url: https://judge.softuni.org/Contests/Practice/Index/1724#2

# --------------- version 1 --------------------

# num_to_receive = int(input())
#
# lst_positives = list()
# lst_negatives = list()
# count_positives = sum_of_negatives = 0
#
# for i in range(num_to_receive):
#     current_num = int(input())
#
#     if current_num < 0:
#         lst_negatives.append(current_num)
#         sum_of_negatives += current_num
#     else:
#         count_positives += 1
#         lst_positives.append(current_num)
#
# print(lst_positives)
# print(lst_negatives)
# print(f'Count of positives: {count_positives}')
# print(f'Sum of negatives: {sum_of_negatives}')

# ---------------- version 2 --------------------

num_to_receive = int(input())

lst_positives = list()
lst_negatives = list()

for i in range(num_to_receive):
    current_num = int(input())

    if current_num < 0:
        lst_negatives.append(current_num)
    else:
        lst_positives.append(current_num)

print(lst_positives)
print(lst_negatives)
print(f'Count of positives: {len(lst_positives)}')
print(f'Sum of negatives: {sum(lst_negatives)}')


