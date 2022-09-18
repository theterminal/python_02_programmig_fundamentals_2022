# 20220712 - Python - Dictionaries - Lecture
# Notes 13


# --------------------------------------------------------------------
print('\n----- dict_1 -------------------------------------------\n\n')


dict_1 = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen'
}
print(dict_1)
print(dict_1[11])


# ---------------------------------------------------------------------
print('\n\n----- dict_2 -------------------------------------------\n\n')


dict_2 = {
    21: 'twenty-one',
    22: dict_1,
    23: 'twenty-three'
}
print(dict_2)
print(dict_2[22])


# ----------------------------------------------------------------------
print('\n\n----- dict_3 -------------------------------------------\n\n')


dict_3 = {
    31: 'thirty-one',
    32: {41: 'forty-one',
         42: 'forty-two',
         43: 'forty-three'
         },
    33: 'twenty-three'
}
print(dict_3)
print(dict_3[32])
print(dict_3[32][42])
print(dict_3.keys())
print(list(dict_3.keys()))
print(list(dict_3.values()))
print(list(dict_3.items()))
print(list(dict_3[32][42]))
print(list(dict_3[32][42][3]))


# ----------------------------------------------------------------------
print('\n\n--------------------------------------------------------\n\n')
