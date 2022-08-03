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


""" ------------------ Fancy Barcodes ----------------------


A barcode is valid when:

    •	It is surrounded by a "@" followed by one or more "#"
    •	It is at least 6 characters long (without the surrounding "@" or "#")
    •	It starts with a capital letter
    •	It contains only letters (lower and upper case) and digits
    •	It ends with a capital letter


Examples of valid barcodes:         @###Che46sE@##, @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##

Examples of invalid barcodes:       ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#


Next, you have to determine the product group of the item from the barcode.
The product group is obtained by concatenating all the digits found in the barcode.
If there are no digits present in the barcode, the default product group is "00".


Examples:
--------
@#FreshFisH@# -> product group: 00
@###Brea0D@### -> product group: 0
@##Che4s6E@## -> product group: 46


Input:
-----
On the first line, you will be given an integer n – the count of barcodes that you will be receiving next. 
On the following n lines, you will receive different strings.


Output:
------
For each barcode that you process, you need to print a message.
    •	If the barcode is invalid: "Invalid barcode"
    •	If the barcode is valid: "Product group: {product group}"


------------ Test Data ------------


Input 1:
-------
3
@#FreshFisH@#
@###Brea0D@###
@##Che4s6E@##


Output 1:
---------
Product group: 00
Product group: 0
Product group: 46


-------------------------------------


Input 2:
-------
6
@###Val1d1teM@###
@#ValidIteM@#
##InvaliDiteM##
@InvalidIteM@
@#Invalid_IteM@#
@#ValiditeM@#


Output 2:
--------
Product group: 11
Product group: 00
Invalid barcode
Invalid barcode
Invalid barcode
Product group: 00


"""