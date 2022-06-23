# 20220617 - Python Code - Lists Advance - Exercise
# 02 - Next Version - judge: https://judge.softuni.org/Contests/Compete/Index/1731#1


# ------------------ version 4 ------------------------


version = input()
version = int(version.replace('.', ''))
print(version)


# ------------------ version 3 ------------------------

version = [i for i in input().split('.')]
version = str(int(version[0] + version[1] + version[2]) + 1)

print('.'.join(version[i] for i in range(len(version))))


# ------------------- version 2 -----------------------


version = [int(i) for i in input().split('.')]
version[-1] += 1

for i in range(len(version) - 1, -1, -1):
    if version[i] > 9:
        version[i] = 0
        if i - 1 >= 0:
            version[i - 1] += 1

print('.'.join(i for i in [str(i) for i in version]))


# ------------------ version 1 ------------------------


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
