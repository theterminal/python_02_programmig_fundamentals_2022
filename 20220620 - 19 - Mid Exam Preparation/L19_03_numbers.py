# 20220621 - Python Code - Mid Exam Preparation
# 03 - Numbers - judge url: https://judge.softuni.org/Contests/Practice/Index/2474#2


# ------------------------ version 2 --- w/ functions --------------------------


# returns a list with up to 5 numbers in descending order from a given list of numbers
def descending_5_nums(nums_to_sort):
    top_five_above_average = []

    for num in sorted(nums_to_sort)[::-1]:
        if len(top_five_above_average) < 5:
            top_five_above_average.append(num)
        else:
            break

    return ' '.join([str(i) for i in top_five_above_average])


# returns a list with all nums above the average num OR 'No' if such num doesn't exist
def nums_above_average(nums):
    average_num = sum(nums_in) / len(nums_in)

    greater_than_average_num = [i for i in nums if i > average_num]

    if greater_than_average_num:
        return descending_5_nums(greater_than_average_num)
    else:
        return 'No'


nums_in = list(map(int, input().split()))
result = nums_above_average(nums_in)
print(result)


# ------------------------ version 1 --- no function --------------------------


# numbers_in = list(map(int, input().split()))                             # int [-1_000_000 : 1_000_000]
# average_from_numbers_in = sum(numbers_in) / len(numbers_in)
# numbers_out = [i for i in numbers_in if i > average_from_numbers_in]
#
# counter = 0
# result = []
#
# for i in range(len(numbers_out)):
#     counter += 1
#
#     if counter == 6:
#         break
#     max_num = max(numbers_out)
#     result += [max_num]
#     numbers_out.remove(max_num)
#
# result = ' '.join([str(i) for i in result])
#
# if len(result) <= 1:
#     print('No')
# else:
#     print(result)
