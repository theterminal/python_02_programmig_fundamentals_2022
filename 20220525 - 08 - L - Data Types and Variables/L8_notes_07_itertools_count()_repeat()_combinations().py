# 20220608 - Python Code


# https://docs.python.org/3/library/itertools.html#itertools.count


# itertools.count(start=0, step=1)

# Make an iterator that returns evenly spaced values starting with number start.
# Often used as an argument to map() to generate consecutive data points.
# Also, used with zip() to add sequence numbers.
# Roughly equivalent to:
#
# def count(start=0, step=1):
#     # count(10) --> 10 11 12 13 14 ...
#     # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
#     n = start
#     while True:
#         yield n
#         n += step

# When counting with floating point numbers, better accuracy can sometimes be achieved by substituting multiplicative code such as:
# (start + step * i for i in count()).

import itertools

for i in itertools.count(10, 10):
    print(i)
    if i == 50:
        break

print()

# ------------------------------------

for j in itertools.repeat(10, 3):
    print(j)

print()

# ------------------------------------

for k in itertools.combinations((1, 2, 3, 4, 5), 3):
    print(k)
