# 20220527 - Python - Python Fundamentals - L9 - Data Types and Variables
# 05 - Print Part Of The ASCII Table - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#4


# ------------- version 2 --------------------


index_start = int(input())
index_end = int(input())
result = ''

for i in range(index_start, index_end + 1):
    char = chr(i)
    result += char + " "

print(result.strip())                           # .strip() takes out the white space from both sides of the string


# ------------- version 1 --------------------


index_start = int(input())
index_end = int(input())
result = ''

for i in range(index_start, index_end + 1):
    char = chr(i)
    if i == index_end:
        result += char
        break
    result += char + " "

print(result)


# ------------- version 3 --------------------


index_start = int(input())
index_end = int(input())
result = ''

for i in range(index_start, index_end + 1):
    if i == index_end:
        result += chr(i)
        break
    result += chr(i) + " "

print(result)
