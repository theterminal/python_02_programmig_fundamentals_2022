# 20220616 - Python Code - Lists Advance - Lecture
# from lecture - 02


# ------------------------------------------------------------


print([x for x in range(11)])
print(list(range(11)))


# -------------------------- way to use longer numbers --------


print(100000 + 1000000)
print(100_000 + 1_000_000)


# --------------------------------------------------------------


print([num + 1 for num in range(23)])


# --------------------------------------------------------------

nums = [1, -3, 12, 0, 44, 9, 119, -33]

print([True if x % 2 == 0 else -1000 for x in nums])                     # [-1000, -1000, True, True, True, -1000, -1000, -1000]
print([x if x % 2 == 0 else -1000 for x in nums])                        # [-1000, -1000, 12, 0, 44, -1000, -1000, -1000]


# --------------------------------------------------------------


nums = [1, -3, 12, 0, 44, 9, 119, -33, 22, 10]

print([num for num in nums if num % 2 == 0 if num > 5 if num != 10])        # [12, 44, 22]
print([num for num in nums if num % 2 == 0 and num > 5 and num != 10])      # [12, 44, 22]
