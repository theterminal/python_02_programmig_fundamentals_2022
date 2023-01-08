# 20220803 - Python Code - Exam Preparation
# 02 - Destination Mapper - judge url: https://judge.softuni.org/Contests/Practice/Index/2518#1

import re


# ------------------------- version 1 ------------------------ judge: 100%


def string_validation(string):
    pattern = r'\={1}[A-Z]{1}[A-za-z]{2,}\={1}|\/{1}[A-Z]{1}[A-za-z]{2,}\/{1}'
    valid_string = re.findall(pattern, string)
    valid = []

    for el in valid_string:
        sign = el[0]
        valid_el = el.strip(sign)
        valid.append(valid_el)
    return valid


def output(valid):
    print(f"Destinations: {', '.join(valid)}")
    total_len = 0
    for element in valid:
        total_len += len(element)
    print(f"Travel Points: {total_len}")


def destination_mapper():
    string_in = input()

    valid_string = string_validation(string_in)
    output(valid_string)


destination_mapper()
