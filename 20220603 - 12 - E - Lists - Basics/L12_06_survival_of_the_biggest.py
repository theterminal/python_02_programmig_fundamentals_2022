# 22020603 - Python Code - L12 - Lists Basics - Exercise
# 06 - Survival of The Biggest - judge url: https://judge.softuni.org/Contests/Compete/Index/1725#5


# _____________ version 1 ________________


lst_nums_in = list(map(int, input().split(' ')))
nums_to_delete = int(input())

for k in range(nums_to_delete):
    lst_nums_in.remove(min(lst_nums_in))

print(', '.join([str(i) for i in lst_nums_in]))


# _____________ version 2 ________________


list_ints_in = input().split(' ')
n = int(input())

list_ints = [int(i) for i in list_ints_in]
smallest_int = list_ints[0]

while n > 0:
    for j in range(len(list_ints)):
        if list_ints[j] < smallest_int:
            smallest_int = list_ints[j]

    list_ints.remove(smallest_int)
    smallest_int = list_ints[0]
    n -= 1

list_strs = [str(i) for i in list_ints]
print(', '.join(list_strs))


# _____________ version 3 ________________


list_str_in = input().split(' ')
num_to_delete = int(input())

list_ints = [int(i) for i in list_str_in]

for k in range(num_to_delete):
    list_ints.remove(min(list_ints))

list_strs = [str(i) for i in list_ints]
print(', '.join(list_strs))
