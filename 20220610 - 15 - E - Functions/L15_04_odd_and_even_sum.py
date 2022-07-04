# 20220614 - Python Code - Functions - Exercise
# 04 - Odd and Even Sum - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#3


def odd_and_even_sums(z1):
    sum_even = 0
    sum_odd = 0

    for i in range(len(z1)):
        if int(z1[i]) % 2 == 0:
            sum_even += int(z1[i])
        else:
            sum_odd += int(z1[i])

    print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')


num_in = input()
odd_and_even_sums(num_in)
