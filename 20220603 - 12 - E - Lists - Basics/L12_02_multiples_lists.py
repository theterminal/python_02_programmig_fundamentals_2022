# 20220603 - Python Code - L12 - Lists Basics
# 02 - Multiple Lists - judge url: https://judge.softuni.org/Contests/Compete/Index/1725#1

# ----------------- version 1 -------------------------------

factor = int(input())
count = int(input())

list_1 = []
counter = 1

for i in range(factor, factor + count):
    num_to_list = counter * factor
    list_1.append(num_to_list)
    counter += 1

print(list_1)


# ----------------- version 2 -------------------------------

factor = int(input())
count = int(input())

list_1 = []

for i in range(1, count + 1):
    list_1.append(factor * i)

print(list_1)

# -------------------- version 3 -----------------------------

factor = int(input())
count = int(input())

list_1 = list(range(factor, count * factor + 1, factor))
print(list_1)

