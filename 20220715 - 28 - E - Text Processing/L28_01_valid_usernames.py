# 20220715 - Python Code - String Processing - Exercise
# 01 - Valid Username - judge url: https://judge.softuni.org/Contests/Compete/Index/1740#0


# ------------------------ version 3 -------------------- judge: 100%


def validate(user_name):
    if 3 <= len(user_name) <= 16:
        if user_name.isalnum() or '-' in user_name or '_' in user_name:
            if ' ' not in user_name:
                return True
    else:
        return False


data_in = input().split(', ')

for user_n in data_in:
    if validate(user_n):
        print(user_n)


# ------------------------ version 2 -------------------- judge: 100%


def length_validation(user_n):
    if 3 <= len(user_n) <= 16:
        return True
    return False


def char_validation(user_n):
    for char in user_n:
        if user_n.isalnum() or '-' in user_n or '_' in user_n:
            return True
    return False


def redundant_symbol_validation(user_n):
    if ' ' not in user_n:
        return True
    return False


def rapper_of_3(user_n):
    if length_validation(user_n) and char_validation(user_n) and redundant_symbol_validation(user_n):
        return True
    return False


data_in = input().split(', ')
for u_name in data_in:
    if rapper_of_3(u_name):
        print(u_name)


# ------------------------ version 1 -------------------- judge: 100%


data_in = input().split(', ')

for u_name in data_in:
    if not (2 < len(u_name) < 17):
        continue
    if not (u_name.isalnum() or '-' in u_name or '_' in u_name):
        continue
    print(u_name)
