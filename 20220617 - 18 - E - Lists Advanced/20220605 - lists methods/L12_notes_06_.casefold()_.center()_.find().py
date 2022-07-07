# 20220612 - Python Code - L12 - Lists Basics - Exersice
# Notes 06

# -------------------------- .casefold() ------------------------
print('\n\n----- ex. 1 ----- .casefold() --------------------\n\n')


# casefold()    - Converts string into lower case


str_10 = 'This is a test string'
print(str_10, '- original string')
print(str_10.casefold(), '- result after .casefold()')


# -------------------------- .center() --------------------------
print('\n\n----- ex. 2 ----- .center() ----------------------\n\n')


# center()      - Returns a centered string with specified total length (string + surrounding symbol)


str_20 = ' This is a centered string '

print('"', str_20, '"', '                        - original string')
print(str_20.center(50, 'k'), '     - the result')


# -------------------------- .find() -----------------------------
print('\n\n----- ex. 3 ----- .find() ------------------------\n\n')


# find()	    - Searches the string for a specified value and returns the position of where it was found
#               - It returns -1 if value is not found. That is the difference with .index()

str_30 = 'This is a string 3 and it is a test.'
print(str_30.find('and'), '- That is the start index of the searched value')
