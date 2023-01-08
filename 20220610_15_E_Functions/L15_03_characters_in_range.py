# 20220614 - Python - Functions - Exercise
# 03 - Characters in Range - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#2


# ---------- version 3 --------------------- judge 100%


def char_in_range(z1, z2):
    asc_start = ord(z1)
    asc_end = ord(z2)

    result = []

    for i in range(asc_start + 1, asc_end):
        result.append(chr(i))

    return result


char_1 = input()
char_2 = input()

output = (char_in_range(char_1, char_2))
print(*output)                                  # only line different from the version 2


# ---------- version 2 --------------------- judge 100%


def char_in_range(z1, z2):
    asc_start = ord(z1)
    asc_end = ord(z2)

    result = []

    for i in range(asc_start + 1, asc_end):
        result.append(chr(i))

    return result


char_1 = input()
char_2 = input()

output = (char_in_range(char_1, char_2))
print(' '.join(output))


# ---------- version 1 --------------------- judge 100%


def char_in_range(z1, z2):
    asc_start = ord(z1)
    asc_end = ord(z2)

    result = ''

    for i in range(asc_start + 1, asc_end):
        result += chr(i) + ' '

    return result


char_1 = input()
char_2 = input()

print(char_in_range(char_1, char_2))
