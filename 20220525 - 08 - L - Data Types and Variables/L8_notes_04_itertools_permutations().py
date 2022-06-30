# 20220608 - Python Code
# itertools - Permutations

from itertools import permutations


# Base command is 'permutations(iterable, r)'
# where 'iterable' is a Tuple, 'r' is num elements in the group, from all elements.

# -------------------------------------------
print('\n--------- Example 1 ------------\n')


for i in permutations((1, 2, 3)):               # 'r' parameter can be omitted, and it equals to the max value
    print(i)


# -------------------------------------------
print('\n--------- Example 2 ------------\n')


tup_1 = (1, 2, 3)
for i in permutations(tup_1, 3):                # 'r' parameter cannot exceed the number of elements in the tuple!
    print(i)


# -------------------------------------------
print('\n--------- Example 3 ------------\n')


tup_1 = (1, 2, 3, 4, 5)

for i in permutations(tup_1, len(tup_1) - 1):   # 'r' parameter can be a formula
    print(i)


# -------------------------------------------
print('\n--------- Example 4 ------------\n')


tup_1 = (1, 2, 3)
all_permutations = permutations(tup_1, 3)       # another syntax
for i in all_permutations:
    print(i)


# -------------------------------------------
print('\n--------- Example 5 ------------\n')


print('\nPermutations from Tuple')
for i in permutations((1, 2, 3), 3):        # the correct syntax
    print(i, end=f"   ->   {type(i)}")
    print()


# -------------------------------------------


print('\nPermutations from List')
for i in permutations([1, 2, 3], 3):        # this works fine but syntax should be as Tuple
    print(i, end=f"   ->   {type(i)}")
    print()


# -------------------------------------------


print('\nPermutations from Set')
for i in permutations({1, 2, 3}, 3):        # this works fine but syntax should be as Tuple
    print(i, end=f"   ->   {type(i)}")
    print()
