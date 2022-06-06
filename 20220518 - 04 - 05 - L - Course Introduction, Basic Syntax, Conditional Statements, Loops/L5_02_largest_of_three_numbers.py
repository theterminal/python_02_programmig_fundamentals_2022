# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax
# 02 - Largest of Three Numbers - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#1

num_1, num_2, num_3 = int(input()), int(input()), int(input())

num_largest = max(num_1, num_2, num_3)
print(num_largest)

# ------------------ another version ------------------

num_1, num_2, num_3 = int(input()), int(input()), int(input())

if num_1 > num_2 and num_1 > num_3:
    print(num_1)
elif num_2 > num_1 and num_2 > num_3:
    print(num_2)
else:
    print(num_3)

# ------------------ older version --------------------

num_1, num_2, num_3 = int(input()), int(input()), int(input())

if num_1 > num_2:
    if num_1 > num_3:
        print(num_1)
    else:
        print(num_3)
else:
    if num_2 > num_3:
        print(num_2)
    else:
        print(num_3)
