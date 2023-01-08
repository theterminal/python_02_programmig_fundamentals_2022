# 20220715 - Python Code - String Processing - Exercise
# 05 - Emoticon Finder - judge url: https://judge.softuni.org/Contests/Compete/Index/1740#4


# ------------------------ version 3 -------------------- judge: 80%


str_in = input()

if ':' in str_in:

    while ':' in str_in:
        index = (str_in.index(':'))

        if index != len(str_in) - 1:
            # if str_in[index + 1] == ':':
            #     str_in = str_in[index + 1:]
            #     continue

            print(str_in[index: index + 2])
            str_in = str_in[index + 2:]

            if len(str_in) <= 1:
                break
        else:
            break
