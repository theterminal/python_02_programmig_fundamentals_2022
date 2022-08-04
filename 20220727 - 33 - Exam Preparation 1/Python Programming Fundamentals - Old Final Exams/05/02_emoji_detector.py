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


""" ------------------- Emoji Detector ---------------------


Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
You have to get your cool threshold.
It is obtained by multiplying all the digits found in the input.
The cool threshold could be a huge number, so be mindful.

An emoji is valid when:
    •	It is surrounded by 2 characters, either "::" or "**"
    •	It is at least 3 characters long (without the surrounding symbols)
    •	It starts with a capital letter
    •	Continues with lowercase letters only
    
Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::

You need to count all valid emojis in the text and calculate their coolness.
The coolness of the emoji is determined by summing all the ASCII values of all letters in the emoji.

Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409

You need to print the result of the cool threshold and, after that to take all emojis out of the text,
count them and print only the cool ones on the console.


Input:
-----
    •	On the single input, you will receive a piece of string.
    
    
Output:
------
    •	On the first line of the output, print the obtained Cool threshold in the format:
    
"Cool threshold: {coolThresholdSum}"

    •	On the following line, print the count of all emojis found in the text in format:
    
"{countOfAllEmojis} emojis found in the text. The cool ones are:
{cool emoji 1}
{cool emoji 2}
…
{cool emoji N}"


Constraints:
-----------
There will always be at least one digit in the text!


----------------- Test Data --------------------


Input 1:
-------
In the Sofia Zoo there are 311 animals in total! ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::. ::Mooning:: **Shy**


Output 1:
--------
Cool threshold: 540
4 emojis found in the text. The cool ones are:
::Smiley:: 
**Tigers** 
::Mooning::


------------------------------------------------


Input 2:
-------
5, 4, 3, 2, 1, go! The 1-th consecutive banana-eating contest has begun! ::Joy:: **Banana** ::Wink:: **Vali** ::valid_emoji::


Output 2:
--------
Cool threshold: 120
4 emojis found in the text. The cool ones are:
::Joy::
**Banana**
::Wink::
**Vali**


------------------------------------------------


Input 3:
-------
It is a long established fact that 1 a reader will be distracted by 9 the readable content of a page when looking at its layout. The point of using ::LoremIpsum:: is that it has a more-or-less normal 3 distribution of 8 letters, as opposed to using 'Content here, content 99 here', making it look like readable **English**.


Output 3:
--------
Cool threshold: 17496
1 emojis found in the text. The cool ones are:


------------------------------------------------

"""
