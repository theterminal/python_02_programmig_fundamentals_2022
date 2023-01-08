# 20220617 - Python - Lists Advance - Exercise
# 02 - Next Version - judge: https://judge.softuni.org/Contests/Compete/Index/1731#1


# ------------------ version 4 ------------------------ judge 100%
# This version will add a number above version 9.9.9  -  it'll become 1.0.0.0 and NOT 10.9.9


version = str(int(input().replace('.', '')) + 1)
result = ''

for i in version:
    result += i + '.'

print(result[:-1:])


# ------------------ version 3 ------------------------ judge 100%


version = [i for i in input().split('.')]
version = str(int(version[0] + version[1] + version[2]) + 1)

print('.'.join(version[i] for i in range(len(version))))


# ------------------- version 2 ----------------------- judge 100%


version = [int(i) for i in input().split('.')]
version[-1] += 1

for i in range(len(version) - 1, -1, -1):
    if version[i] > 9:
        version[i] = 0
        if i - 1 >= 0:
            version[i - 1] += 1

print('.'.join(i for i in [str(i) for i in version]))


# ------------------ version 1 ------------------------ judge 100%


version = [int(i) for i in input().split('.')]

if version[2] + 1 > 9:
    if version[1] + 1 > 9:
        version[0] += 1
        version[1] = 0
        version[2] = 0
    else:
        version[1] += 1
        version[2] = 0
else:
    version[2] += 1

print('.'.join(str(version[i]) for i in range(len(version))))
