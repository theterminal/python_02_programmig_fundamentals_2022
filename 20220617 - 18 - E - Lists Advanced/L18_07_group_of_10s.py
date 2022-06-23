# 20220617 - Python Code - Lists Advance - Exercise
# 07 - Group of 10's - judge: https://judge.softuni.org/Contests/Compete/Index/1731#6


lst_in = list(map(int, input().split(', ')))
rng_start = 0
rng_end = 10
lst_out = []
values_to_remove = []

while len(lst_in) > 0:
    for num in lst_in:
        while num in range(rng_start, rng_end + 1):
            lst_out.append(num)
            values_to_remove.append(num)
            break

    print(f'Group of {rng_end}\'s: {lst_out}')
    rng_start += 10
    rng_end += 10
    lst_out.clear()

    for value in values_to_remove:
        lst_in.remove(value)
    values_to_remove.clear()
