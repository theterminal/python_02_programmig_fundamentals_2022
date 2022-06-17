# 20220614 - Python Code - Functions - Exercise
# 04 - Odd and Even Sum - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#3

def odd_and_even_sums(z1):
    str_num = str(z1)

    sum_even = 0
    sum_odd = 0

    for i in range(len(str_num)):
        if int(str_num[i]) % 2 == 0:
            sum_even += int(str_num[i])
        else:
            sum_odd += int(str_num[i])

    print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')


num_in = int(input())
odd_and_even_sums(num_in)
