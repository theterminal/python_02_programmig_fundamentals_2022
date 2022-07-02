# 22020613 - Python Code - L12 - Lists Basics - More Exercise
# 02 - Messaging - judge url: https://judge.softuni.org/Contests/Practice/Index/1726#1


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
