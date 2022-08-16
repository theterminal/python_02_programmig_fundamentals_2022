# 22020613 - Python - L12 - Lists Basics - More Exercise
# 02 - Messaging - judge url: https://judge.softuni.org/Contests/Practice/Index/1726#1


# ______________ version 1 _________________ judge 100%


nums_in = input().split(' ')
str_in = input()

index = 0
message = ''

for i in nums_in:
    for j in range(len(i)):
        index += int(i[j])

    while index > len(str_in):
        index -= len(str_in)

    message += str_in[index]
    str_in = str_in[:index] + str_in[index + 1:]

    index = 0

print(message)


""" _______________ Messaging _______________


On the first line, you will receive a sequence of numbers separated by a single space.
On the second line, you will receive a string.

Your task is to write a program that sends a message only using chars from the given string.
Each char the program adds to the message should be found by its index.
The index you are looking for is the sum of a number's digits from the sequence.
If the index is greater than the length of the text, continue counting from the beginning (so that you always have a valid index).
When you find a char, you should add it to the message and remove it from the string.
It means that for the following index, the text will be with one character less.
Print the final message.


______________ Test Data _______________


Input 1:
-------
9992 562 8933
This is some message for you


Output 1:
--------
hey


----------------------------------------


Input 2:
-------
2 122 1123 1321 9 17211
87j973u59dg37e725!


Output 2:
--------
judge!


---------------------------------------
"""

