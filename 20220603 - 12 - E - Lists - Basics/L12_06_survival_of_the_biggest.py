# 22020603 - Python Code - L12 - Survival of the Biggest
# 06 - Survival of The Biggest - judge url: https://judge.softuni.org/Contests/Compete/Index/1725#5

# list_ints_in = input().split(' ')
# n = int(input())
#
# list_ints = [int(i) for i in list_ints_in]
# smallest_int = list_ints[0]
#
# while n > 0:
#     for j in range(len(list_ints)):
#         if list_ints[j] < smallest_int:
#             smallest_int = list_ints[j]
#
#     list_ints.remove(smallest_int)
#     smallest_int = list_ints[0]
#     n -= 1
#
# list_strs = [str(i) for i in list_ints]
# print(', '.join(list_strs))

# _____________ version 2 ________________

list_str_in = input().split(' ')
num_to_delete = int(input())

list_ints = [int(i) for i in list_str_in]

for k in range(num_to_delete):
    list_ints.remove(min(list_ints))

list_strs = [str(i) for i in list_ints]
print(', '.join(list_strs))