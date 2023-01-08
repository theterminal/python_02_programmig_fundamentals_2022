# 20220712 - Python - Dictionaries - Lecture
# Note - 04 - Dictionaries, .split()


given_stock = 'cheese 10 bread 5 ham 10 chocolate 3'        # given string separated by space
dict_from_given_stock = {}                                  # creating an empty dictionary
given_stock = given_stock.split(' ')                        # list created from the given string
print(given_stock)

for i in range(0, len(given_stock), 2):                     # loop to fill in the dictionary with 'key-value' pairs
    key = given_stock[i]
    value = given_stock[i + 1]
    dict_from_given_stock[key] = int(value)

print(dict_from_given_stock)
