# 20220715 - Python Code - String Processing - Exercise
# 10 - Winning Ticket - judge url: https://judge.softuni.org/Contests/Compete/Index/1740#9


# ------------------------ version 1 -------------------- judge: 100%


def valid_ticket(string):
    if len(string) == 20:
        return True
    return False


def winning_ticket(string):
    side_l = string[0: 10]
    side_r = string[10:]
    count_l = 0
    count_r = 0
    max_l = 0
    max_r = 0
    symbol_out = ''

    for symbol in winning_symbols:
        if side_l.count(symbol) == 10 and side_r.count(symbol) == 10:
            return f'ticket "{20 * symbol}" - 10{symbol} Jackpot!'

    for symbol in winning_symbols:
        for s in side_l:
            if s == symbol:
                count_l += 1
                if count_l > max_l:
                    max_l = count_l
                    symbol_out = symbol
            else:
                count_l = 0

        for s in side_r:
            if s == symbol:
                count_r += 1
                if count_r > max_r:
                    max_r = count_r
                    symbol_out = symbol
            else:
                count_r = 0

    result = min(max_l, max_r)
    if result >= 6:
        return f'ticket "{string}" - {result}{symbol_out}'
    else:
        return f'ticket "{string}" - no match'


data_in = [n.strip() for n in input().split(', ')]
winning_symbols = ['@', '#', '$', '^']

for ticket in data_in:
    if valid_ticket(ticket):
        print(winning_ticket(ticket))
    else:
        print('invalid ticket')
