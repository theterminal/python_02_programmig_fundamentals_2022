# 20220608 - Python Code - Functions - Lecture
# 06 - map(), sorted()

# ------- input str of numbers mapped to integers in a list --------


print('\n------- enter the string of numbers -------\n')
# must enter the numbers: 1, 2, 3, 4, 5, 6, 7

numbers = list(map(int, input().split(', ')))

print(numbers)
print(type(numbers))

print()
for i in numbers:
    print(type(i))


# ------------------- number on a power ---------------------------


print('\n------- power of nums with function and map() -------\n')

numbers = [1, 2, 3, 4, 5, 6, 7]


def power_of_nums(num):
    return num * num


powers = list(map(power_of_nums, numbers))
print(powers)

# ------------------- sorted() -----------------------------------


print('\n------- sorted() -------------------------------------\n')

numbers = [19, -4, 13, 0, 5, 7, 7]
print(sorted(numbers))
