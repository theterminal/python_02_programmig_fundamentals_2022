# 20220715 - Python Code - String Processing - Exercise
# 06 - Replace Repeating Chars - judge url: https://judge.softuni.org/Contests/Compete/Index/1740#5


# ------------------------ version 1 -------------------- judge: 100%


data_in = input()
chars_to_print = ''
last_char = ''

for i in range(len(data_in)):
    if i == 0:
        chars_to_print = data_in[i]
        last_char = data_in[i]
        continue

    if data_in[i] == last_char:
        continue
    else:
        chars_to_print += data_in[i]
        last_char = data_in[i]

print(chars_to_print)
