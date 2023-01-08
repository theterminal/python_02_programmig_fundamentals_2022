# 20220714 - Python - String Processing - Lecture
# 01 - Reverse Strings - judge url: https://judge.softuni.org/Contests/Practice/Index/1739#0


# ------------------- version 1 ------------ slicing ---------- judge: 100%


while True:
    data_in = input()
    if data_in == 'end':
        break

    print(f'{data_in} = {data_in[::-1]}')


# ------------------- version 2 ------------ reversed ---------- judge: 100%


rev_d = ''

while True:
    data_in = input()
    if data_in == 'end':
        break

    for i in reversed(data_in):
        rev_d += i

    print(data_in, '=', rev_d)
    rev_d = ''


# ------------------- version 3 ------------ reversed ---------- judge: 100%


while True:
    data_in = input()
    if data_in == 'end':
        break

    print(f'{data_in} = {"".join(reversed(data_in))}')
