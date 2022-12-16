# 20220712 - Python - Dictionaries - Lecture
# Note 13 - Nested dictionaries


print('\n__________ dict_1 __________\n')


dict_1 = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen'
}

print(dict_1)                  # {11: 'eleven', 12: 'twelve', 13: 'thirteen'}
print(dict_1[11])              # eleven


print('\n__________ dict_2 __________\n')


dict_2 = {
    21: 'twenty-one',
    22: dict_1,
    23: 'twenty-three'
}

print(dict_2)                 # {21: 'twenty-one', 22: {11: 'eleven', 12: 'twelve', 13: 'thirteen'}, 23: 'twenty-three'}
print(dict_2[22])             # {11: 'eleven', 12: 'twelve', 13: 'thirteen'}


print('\n__________ dict_3 __________\n')


dict_3 = {
    31: 'thirty-one',
    32: {41: 'forty-one',
         42: 'forty-two',
         43: 'forty-three'
         },
    33: 'twenty-three'
}

print(dict_3)                       # {31: 'thirty-one', 32: {41: 'forty-one', 42: 'forty-two', 43: 'forty-three'}, 33: 'twenty-three'}
print(dict_3[32])                   # {41: 'forty-one', 42: 'forty-two', 43: 'forty-three'}
print(dict_3[32][42])               # forty-two
print(dict_3.keys())                # dict_keys([31, 32, 33])
print(list(dict_3.keys()))          # [31, 32, 33]
print(list(dict_3.values()))        # ['thirty-one', {41: 'forty-one', 42: 'forty-two', 43: 'forty-three'}, 'twenty-three']
print(list(dict_3.items()))         # [(31, 'thirty-one'), (32, {41: 'forty-one', 42: 'forty-two', 43: 'forty-three'}), (33, 'twenty-three')]
print(list(dict_3[32][42]))         # ['f', 'o', 'r', 't', 'y', '-', 't', 'w', 'o']
print(list(dict_3[32][42][3]))      # ['t']
