# 20220617 - Python Code - Lists Advance - Exercise
# 01 - Which Are In - judge: https://judge.softuni.org/Contests/Compete/Index/1731#0


# ----------------------------- version 1 --------------------------


lst_1 = input().split(', ')
lst_2 = input().split(', ')

result = []

for i in lst_1:
    for j in range(len(lst_2)):
        if i in lst_2[j]:
            result.append(i)
            break

print(result)


# ----------------------------- version 2 --------------------------


lst_1 = input().split(', ')
lst_2 = input().split(', ')

result = []

for i in lst_1:
    for j in lst_2:
        if i in j:
            result.append(i)
            break

print(result)
