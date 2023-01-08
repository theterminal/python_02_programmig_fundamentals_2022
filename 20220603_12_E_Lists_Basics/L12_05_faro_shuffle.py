# 20220603 - Python - L12 - Lists Basics - Exercise
# 05 - Faro Shuffle - judge url: https://judge.softuni.org/Contests/Compete/Index/1725#4


# ------------------------ version 1 -------------------------- judge 100%


lst_cards_given = input().split(' ')
num_shuffles = int(input())

len_cards_given_dev_2 = int(len(lst_cards_given) / 2)               # can use 'len // 2' and it'll be no problem for int!
lst_cards_to_work_with = lst_cards_given.copy()
lst_to_shuffle = []

while num_shuffles > 0:
    lst_left = lst_cards_to_work_with[:len_cards_given_dev_2]
    lst_right = lst_cards_to_work_with[len_cards_given_dev_2::]

    for i in range(len_cards_given_dev_2):
        lst_to_shuffle.append(lst_left[i])
        lst_to_shuffle.append(lst_right[i])

    lst_cards_to_work_with = lst_to_shuffle.copy()
    lst_to_shuffle.clear()
    num_shuffles -= 1

print(lst_cards_to_work_with)
