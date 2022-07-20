# 20220712 - Python Code
# Fibonacci Sequence, Tribonacci Sequence :)


# ------------------- fibonacci sequence -------------------------------


def fibonacci(n):
    """Prints a Fibonacci sequence up to 'n'."""

    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fibonacci(1000)


# ------------------- tribonacci sequence -------------------------------


def tribonacci(n):
    """Prints a Tribonacci :) sequence up to 'n'."""

    a, b, c = 0, 1, 2
    while a < n:
        print(a, end=' ')
        a, b, c = b, c,  a + b + c
    print()


tribonacci(1000)
