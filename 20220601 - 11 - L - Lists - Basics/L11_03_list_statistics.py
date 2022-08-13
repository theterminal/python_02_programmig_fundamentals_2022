# 20220601 - Python Code - L11 - Lists - Basics
# 03 - List Statistics - judge url: https://judge.softuni.org/Contests/Practice/Index/1724#2


# --------------------- version 1 -------------------------- judge 100%


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


""" ---------------- List Statistics -----------------


On the first line, you will receive a number 'n'.
On the following 'n' lines, you will receive integers.

You should create and print two lists:
    •	One with all the positives (including 0) numbers
    •	One with all the negatives numbers

Finally, print the following message:

"Count of positives: {count_positives}
Sum of negatives: {sum_of_negatives}"


----------- Test Data --------------


Input 1:
-------
5
10
3
2
-15
-4


Output 1:
--------
[10, 3, 2]
[-15, -4]
Count of positives: 3
Sum of negatives: -19


------------------------------------


Input 2:
-------
6
11
2
35
599
31
20


Output 2:
--------
[11, 2, 35, 599, 31, 20]
[]
Count of positives: 6
Sum of negatives: 0


------------------------------------

"""
