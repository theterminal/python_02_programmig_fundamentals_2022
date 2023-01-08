# 20220715 - Python Code - String Processing - Exercise
# 09 - Rage Quit - judge url: https://judge.softuni.org/Contests/Compete/Index/1740#8


# ------------------------ version 3 -------------------- judge: 100%


data_in = input().upper()

symbols_to_multiply = ''
num_to_multiply = ''
output = ''

for index in range(len(data_in)):
    if not data_in[index].isdigit():
        symbols_to_multiply += data_in[index]
    else:
        num_to_multiply += data_in[index]

        for index_plus_1 in range(index + 1, len(data_in)):
            if not data_in[index_plus_1].isdigit():
                break
            num_to_multiply += data_in[index_plus_1]

        output += int(num_to_multiply) * symbols_to_multiply
        symbols_to_multiply = ''
        num_to_multiply = ''

print(f'Unique symbols used: {len(set(output))}')
print(output)


# ------------------------ version 2 -------------------- judge: 100%


data_in = input().upper()

symbols_to_multiply = ''
num_to_multiply = ''
output = ''

for index in range(len(data_in)):
    if not data_in[index].isdigit():
        symbols_to_multiply += data_in[index]
    else:
        for index_symbol in range(index, len(data_in)):
            if not data_in[index_symbol].isdigit():
                break
            num_to_multiply += data_in[index_symbol]

        output += int(num_to_multiply) * symbols_to_multiply
        symbols_to_multiply = ''
        num_to_multiply = ''

print(f'Unique symbols used: {len(set(output))}')
print(output)


# ------------------------ version 1 -------------------- judge: 71%


data_in = input().upper()

symbols_to_multiply = ''
num_to_multiply = ''
output = ''

for symbol in data_in:
    if not symbol.isdigit():
        symbols_to_multiply += symbol
    else:
        index = data_in.index(symbol)

        for i in range(index, len(data_in)):
            if not data_in[i].isdigit():
                break
            num_to_multiply += data_in[i]

        output += symbols_to_multiply * int(num_to_multiply)
        symbols_to_multiply = ''
        num_to_multiply = ''

print(f'Unique symbols used: {len(set(output))}')
print(output)
