# 20220618 - Python - Lists Advance - Exercise
# 08 - Decipher This - judge: https://judge.softuni.org/Contests/Compete/Index/1731#7


# ---------------- version 01 ------------------------------ judge 100%


message_in = input().split()
message = ''

for word in message_in:
    num = alpha = ''

    for i in range(len(word)):
        if word[i].isdigit():
            num += word[i]
        else:
            alpha += word[i]

    letter_from_num = chr(int(num))

    if len(alpha) > 1:
        alpha_new = alpha[-1] + alpha[1:-1] + alpha[0]
    else:
        alpha_new = alpha

    message += (letter_from_num + alpha_new) + ' '

print(message)


# ---------------- version 02 ------------------------------ judge 100%


str_in = input().split()

ascii_letter = full_word = ''

for word in str_in:
    for i in range(len(word)):
        if word[i].isdigit():
            ascii_letter += word[i]
        else:
            break

    length_asc = len(ascii_letter)
    ascii_letter = chr(int(ascii_letter))

    if (len(word) - length_asc) > 1:
        alpha_new = word[-1] + word[length_asc + 1: -1] + word[length_asc]
    else:
        alpha_new = word[-1]

    full_word += (ascii_letter + alpha_new) + ' '
    ascii_letter = ''

print(full_word)


# ---------------- version 03 ------------------------------ judge 100%


str_in = input().split()

ascii_letter = ''
alpha_word = ''
full_word = ''

for word in str_in:
    for i in range(len(word)):
        if word[i].isdigit():
            ascii_letter += word[i]

        if word[i].isalpha():
            alpha_word += word[i]

    ascii_letter = chr(int(ascii_letter))
    if len(alpha_word) > 1:
        alpha_new = alpha_word[-1] + alpha_word[1:-1] + alpha_word[0]
    else:
        alpha_new = alpha_word

    full_word += (ascii_letter + alpha_new) + ' '
    ascii_letter = ''
    alpha_word = ''
print(full_word)
