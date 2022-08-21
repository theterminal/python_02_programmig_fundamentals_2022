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


""" _____________ Next Version ______________


You are fed up with changing the version of your software manually.
Instead, you will create a little script that will make it for you.

You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".

Your task is to print the next version.

For example, if the current version is "1.3.4", the next version will be "1.3.5". 
The only rule is that the numbers cannot be greater than 9.
If it happens, set the current number to 0 and increase the previous number.
For more clarification, see the examples below.
 
Note: there will be no case in which the first number will become greater than 9.


___________ Test Data ___________


Input 1:
-------
1.2.3


Output 1:
--------
1.2.4


---------------------------------


Input 2:
-------
1.3.9


Output 2:
--------
1.4.0


---------------------------------


Input 3:
-------
3.9.9


Output 3:
--------
4.0.0


---------------------------------
"""
