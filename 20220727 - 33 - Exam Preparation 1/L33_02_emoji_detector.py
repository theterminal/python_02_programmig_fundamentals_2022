# 20220731 - Python - Exam Preparation 1
# 02 - Emoji Detector - judge url: https://judge.softuni.org/Contests/Practice/Index/2302#1

import re

# ------------------------- version 1 ---------- no function --------- judge: 100%


data = input()

pattern_num = r'\d'
match = re.findall(pattern_num, data)
cool_threshold = sum_emoji = 0

for i in range(len(match)):
    if i == 0:
        cool_threshold += int(match[i])
    else:
        cool_threshold *= int(match[i])

print(f'Cool threshold: {cool_threshold}')

pattern_valid_emoji = r'(\:{2}[A-Z][a-z]{2,}\:{2}|\*{2}[A-Z][a-z]{2,}\*{2})'
valid_emojis = re.findall(pattern_valid_emoji, data)

print(f'{len(valid_emojis)} emojis found in the text. The cool ones are:')

for emoji in valid_emojis:
    for char in range(len(emoji)):
        if 1 < char < len(emoji) - 2:
            sum_emoji += ord(emoji[char])

    if sum_emoji >= cool_threshold:
        print(emoji)

    sum_emoji = 0


# ------------------------- version 2 ---------- function --------- judge: 100%


def f_cool_threshold(data):
    pattern_1 = r'\d'
    match = re.findall(pattern_1, data)
    cool_threshold = 0

    for i in range(len(match)):
        if i == 0:
            cool_threshold += int(match[i])
        else:
            cool_threshold *= int(match[i])
    return cool_threshold


def f_valid_emoji(data):
    pattern_valid_emoji = r'(\:{2}[A-Z][a-z]{2,}\:{2}|\*{2}[A-Z][a-z]{2,}\*{2})'
    valid_emojis = re.findall(pattern_valid_emoji, data)
    return valid_emojis


def f_cool_emojis(valid_emojis, cool_threshold):
    sum_emoji = 0

    for emoji in valid_emojis:
        for char in range(len(emoji)):
            if 1 < char < len(emoji) - 2:
                sum_emoji += ord(emoji[char])

        if sum_emoji >= cool_threshold:
            print(emoji)

        sum_emoji = 0


def emoji_detector():
    data = input()

    cool_threshold = f_cool_threshold(data)
    print(f'Cool threshold: {cool_threshold}')

    valid_emojis = f_valid_emoji(data)
    print(f'{len(valid_emojis)} emojis found in the text. The cool ones are:')

    f_cool_emojis(valid_emojis, cool_threshold)


emoji_detector()
