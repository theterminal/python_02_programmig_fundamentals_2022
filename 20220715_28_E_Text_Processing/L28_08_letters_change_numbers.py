# 20220715 - Python Code - String Processing - Exercise
# 08 - Letters Change Numbers - judge url: https://judge.softuni.org/Contests/Compete/Index/1740#7


# ------------------------ version 1 -------------------- judge: 80%


data_in = input().split(' ')
data = []

num = ''
total_sum = 0

for i in data_in:
    if len(i) == 0:
        continue
    data.append(i.strip())

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for j in data:

    if j[0].isupper():
        if j[-1].isupper():
            num = (float(j[1: -1]) / (alphabet.index(j[0].lower()) + 1)) - (alphabet.index(j[-1].lower()) + 1)
        else:
            num = (float(j[1: -1]) / (alphabet.index(j[0].lower()) + 1)) + (alphabet.index(j[-1].lower()) + 1)
    else:
        if j[-1].isupper():
            num = ((float(j[1: -1])) * (alphabet.index(j[0].lower()) + 1)) - (alphabet.index(j[-1].lower()) + 1)
        else:
            num = ((float(j[1: -1])) * (alphabet.index(j[0].lower()) + 1)) + (alphabet.index(j[-1].lower()) + 1)

    total_sum += num
    num = 0

print(f'{total_sum:.2f}')
