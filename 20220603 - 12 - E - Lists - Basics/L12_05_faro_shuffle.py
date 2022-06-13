# 20220603 - Python Code - L12 - Lists Basics - E
# 05 - Faro Shuffle - judge url: https://judge.softuni.org/Contests/Compete/Index/1725#4

lst_cards_given = input().split(' ')
num_shuffles = int(input())

len_cards_given_dev_2 = int(len(lst_cards_given) / 2)               # can use 'len // 2' and it'll be no problem for int!
lst_cards_to_work_with = lst_cards_given.copy()
lst_to_print = []


while num_shuffles > 0:
    lst_left = lst_cards_to_work_with[:len_cards_given_dev_2]
    lst_right = lst_cards_to_work_with[len_cards_given_dev_2::]

    for i in range(len_cards_given_dev_2):
        lst_to_print.append(lst_left[i])
        lst_to_print.append(lst_right[i])

    lst_cards_to_work_with = lst_to_print.copy()
    lst_to_print.clear()
    num_shuffles -= 1

print(lst_cards_to_work_with)
