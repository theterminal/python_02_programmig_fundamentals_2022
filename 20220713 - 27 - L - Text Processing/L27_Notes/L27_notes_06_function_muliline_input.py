# 20220715 - Python
# Note 06 - Function for Entering Multiline Input


# Keep entering lines of input, when done enter [space] to end the program
def multiline_input_function(text):
    print(text)
    multiline_input: str = ''

    while True:
        data_in = input()

        if data_in == '':
            break
        multiline_input += data_in + '\n'

    return multiline_input


an_instance = multiline_input_function('Enter your words: ')

print(an_instance)
print(type(an_instance))
