# 20220617 - Python - Lists Advance - Lecture
# 06 - Even Numbers - judge: https://judge.softuni.org/Contests/Practice/Index/1730#5


# ----------------- version 1 ------------------- judge 100%


numbers = list(map(int, input().split(', ')))
indices = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]

print(indices)
