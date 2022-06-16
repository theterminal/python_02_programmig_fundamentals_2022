# 20220608 - Python Code - Functions - Lecture
# 04 - Function Odd / Even Number


def odd_even(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


num_to_test = int(input())
print(odd_even(num_to_test))
