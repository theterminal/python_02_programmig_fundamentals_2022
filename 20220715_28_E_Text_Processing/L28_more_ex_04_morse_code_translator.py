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
