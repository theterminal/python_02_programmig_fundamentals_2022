# 20220527 - Python - Python Fundamentals - L9 - Data Types and Variables
# 06 - Triples Of Latin Letters - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#5


num_letters = int(input())
ascii_range = range(97, 97 + num_letters)

for char_1 in ascii_range:
    for char_2 in ascii_range:
        for char_3 in ascii_range:

            print(f'{chr(char_1)}{chr(char_2)}{chr(char_3)}')
