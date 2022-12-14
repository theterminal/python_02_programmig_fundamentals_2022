# 20220612 - Python - L12 - Lists Basics - Exersice
# Note 06


print('\n\n----- ex. 1 ----- .casefold() --------------------\n\n')


# casefold()    - Converts string into lower case


str_10 = 'THIS IS A TEST STRING'

print(str_10)                                                               # THIS IS A TEST STRING
print(str_10.casefold())                                                    # this is a test string


print('\n\n----- ex. 2 ----- .center() ----------------------\n\n')


# center()      - Returns a centered string with specified total length (string + surrounding symbol)


str_20 = 'This is a centered string'

print(str_20)                                                              # This is a centered string
print(str_20.center(40, 'k'))                                              # kkkkkkkThis is a centered stringkkkkkkkk


print('\n\n----- ex. 3 ----- .find() ------------------------\n\n')


# find()	    - Searches the string for a specified value and returns the position where it begins.
#               - It returns -1 if value is not found. That is the difference with ".index()"

str_30 = 'This is test string 3 and it is a test.'
print(str_30.find('test'))                                                  # 8
