# 20220614 - Python Code - Functions - Exercise
# 09 - Password Validator - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#8


# -------------- version 3 --- using 3 functions, .isalnum(), .isdigit(), validate all ------------------


def length_is_valid(some_string):
    if 6 <= len(some_string) <= 10:
        return True
    print('Password must be between 6 and 10 characters')
    return False


def symbols_are_valid(some_string):
    if some_string.isalnum():
        return True
    print('Password must consist only of letters and digits')
    return False


def has_min_2_digits(some_string):
    digit_counter = 0
    for i in some_string:
        if i.isdigit():
            digit_counter += 1

    if digit_counter >= 2:
        return True
    print('Password must have at least 2 digits')
    return False


password = input()
validate = [length_is_valid(password), symbols_are_valid(password), has_min_2_digits(password)]

# print(validate)                                           # example result [True, False, False]

if all(validate):
    print('Password is valid')


# -------------- version 2 --- using 1 function, .isalnum(), .isdigit() ---------------------------------


def pass_validator(test_in: str):

    # Length of the password must be [6:10]
    if not (6 <= len(test_in) <= 10):
        print('Password must be between 6 and 10 characters')
        return

    # Only alphanumeric chars must be used
    if not (test_in.isalnum()):
        print('Password must consist only of letters and digits')
        return

    # Must contain at leas 2 digits
    count_digits = 0

    for i in test_in:
        if i.isdigit():
            count_digits += 1
    else:
        if count_digits < 2:
            print('Password must have at least 2 digits')
            return

    print('Password is valid')


pass_in = input()
pass_validator(pass_in)


# -------------- version 1 --- using 1 function -----------------------------------------------


def pass_validator(test_in: str):

    # Length of the password must be [6:10]
    if not (6 <= len(test_in) <= 10):
        print('Password must be between 6 and 10 characters')
        return

    # Only alphanumeric chars must be used
    for i in test_in:
        if not (48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122):
            print('Password must consist only of letters and digits')
            flag = True
            return

    # Must contain at leas 2 digits
    count_digits = 0

    for i in test_in:
        if 48 <= ord(i) <= 57:
            count_digits += 1
    else:
        if count_digits < 2:
            print('Password must have at least 2 digits')
            return

    print('Password is valid')


pass_in = input()
pass_validator(pass_in)
