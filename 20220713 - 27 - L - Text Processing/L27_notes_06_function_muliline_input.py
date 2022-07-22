# 20220715 - Python Code
# Notes 06 - Function for Entering Multiline Input


def multiline_input_function(text):
    print(text)
    multiline_input: str = ''

    while True:
        data_in = input()

        if data_in != '':
            multiline_input += data_in + '\n'
        else:
            break

    return multiline_input


an_instance = multiline_input_function('Enter your words: ')

print(an_instance)
print(type(an_instance))
