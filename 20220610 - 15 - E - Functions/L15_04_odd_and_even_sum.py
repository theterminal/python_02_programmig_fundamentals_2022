# 20220614 - Python Code - Functions - Exercise
# 04 - Odd and Even Sum - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#3


# ---------- version 1 ---------- judge 100%


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


""" ______________ Odd and Even Sum _______________


You will receive a single number.
You should write a function that returns the sum of all even and all odd digits in a given number.

The result should be returned as a single string in the format:
"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

Print the result of the function on the console.


___________ Test Data _____________


Input 1:
-------
1000435


Output 1:
--------
Odd sum = 9, Even sum = 4


-----------------------------------


Input 2:
-------
3495892137259234


Output 2:
--------
Odd sum = 54, Even sum = 22


-----------------------------------
"""
