# 20220729 - Python Code - Exam Preparation 2
# 02 - Fancy Barcodes - judge url: https://judge.softuni.org/Contests/Practice/Index/2303#1

import re


# ------------------------- version 2 ------------------------ judge: 100%


num_barcodes = int(input())
num = ''

pat_1 = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'
pat_2 = r'\d'

for i in range(num_barcodes):
    barcode = input()
    match_1 = re.match(pat_1, barcode)

    if match_1:
        match_2 = re.findall(pat_2, barcode)
        if match_2:
            num = ''.join(match_2)
            print(f'Product group: {num}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')


# ------------------------- version 1 ------------------------ judge: 100%


num_barcodes = int(input())
num = ''

# pat_1 = r'@[#]+[A-Z]+([A-Za-z0-9]+){4,}[A-Z]@[#]+' - That one works also
# pat_1 = r'\@\#+[A-Z][A-Za-z0-9]{4,}[A-Z]\@\#+' - That one works also
pat_1 = r'\@\#+[A-Z][A-Za-z0-9]{4,}[A-Z]\@\#+'

for i in range(num_barcodes):
    barcode = input()
    match_1 = re.match(pat_1, barcode)

    if match_1:
        for char in barcode:
            if char.isdigit():
                num += char

        if len(num) == 0:
            num = '00'

        print(f'Product group: {num}')
        num = ''
    else:
        print('Invalid barcode')
