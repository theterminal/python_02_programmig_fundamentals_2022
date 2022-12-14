# 20220617 - Python - Lists Advance - Exercise
# 03 - Word Filter - judge: https://judge.softuni.org/Contests/Compete/Index/1731#2


# -------------- version 1 ---------------------------------- judge 100%


lst_text = input().split(' ')

for i in [j for j in lst_text if len(j) % 2 == 0]:
    print(i)


# -------------- version 2 ---------------------------------- judge 100%


for i in [j for j in input().split(' ') if len(j) % 2 == 0]:
    print(i)


# -------------- version 3 ---------------------------------- judge 100%


print('\n'.join([i for i in input().split() if len(i) % 2 == 0]))
