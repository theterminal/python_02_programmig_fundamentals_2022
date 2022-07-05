# 20220615 - Python Code - Functions - Exercise
# 11 - Loading Bar - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#10


def loading_bar(num):
    if num == 100:
        return f'{num}% Complete!\n[%%%%%%%%%%]'

    bar_l = int(num / 10) * '%'
    bar_r = (10 - int(num / 10)) * '.'
    bar = bar_l + bar_r
    return f'{num}% [{bar}]\nStill loading...'


int_input_div_10 = int(input())
print(loading_bar(int_input_div_10))
