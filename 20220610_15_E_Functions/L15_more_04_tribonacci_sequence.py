# 20220615 - Python - Functions - More Exercise
# 04 - Tribonacci Sequence - judge url: https://judge.softuni.org/Contests/Practice/Index/1729#3


# -------------- version 1 -------------------------- judge 100%


def tribonacci(num):
    output = [1]

    for i in range(1, num):
        output.append(sum(output[-1: -4: -1]))
    return [str(k) for k in output]


num_end = int(input())
result = tribonacci(num_end)

print(' '.join(result))
