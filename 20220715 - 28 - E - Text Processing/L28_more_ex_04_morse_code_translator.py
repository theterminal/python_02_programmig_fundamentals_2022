# 20220721 - Python Code - String Processing - Exercise
# More Exercise 04 - Morse Code Translator - judge url: https://judge.softuni.org/Contests/Practice/Index/1741#3


# --------------------- version 1 -------------------- judge: 100%


dict_morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
}

morse_in = input().split(' | ')
letter_converted = ''
word_converted = ''
letters_in_word = ''

for word in morse_in:
    letters_in_word = word.split(' ')

    for letter in letters_in_word:
        for k, v in dict_morse.items():
            if letter == v:
                word_converted += k.upper()

    print(word_converted, end=' ')
    word_converted = ''


""" _________________ Morse Code Translator ____________


Write a program that translates messages from Morse code to English (capital letters only).
Use this link (https://morsecode.scphillips.com/morse2.html) (KK – the page has changed)
[KK note: This one works -> https://morsecode.world/american/morse.html]

The words (letters is more accurate) will be separated by a space ' '.
Each word is separated by a ' | '.
Print the found words on one line, separated by a space ' '.


______________________ Example __________________________


Input 1:
---------
.. | -- .- -.. . |  -.-- --- ..- | .-- .-. .. - . | .- | .-.. --- -. --. | -.-. --- -.. .


Output 1:
---------
I MADE YOU WRITE A LONG CODE

__________________________________________________________


Input 2:
---------

.. | .... --- .--. . | -.-- --- ..- | .- .-. . | -. --- - | -- .- -..


Output 2:
---------

I HOPE YOU ARE NOT MAD


__________________________________________________________

"""
