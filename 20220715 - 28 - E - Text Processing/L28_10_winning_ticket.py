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


""" ---------------- Winning Ticket -------------------------


The lottery is exciting.
However, checking a million tickets for winnings only by hand is not.
So, you are given the task of creating a program that automatically checks if a ticket is a winner.

You are given a collection of tickets separated by commas and spaces (one or many).
You need to check each ticket to see if it has a winning combination of symbols:

•	A valid ticket has exactly 20 characters.
•	A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly, repeated at least 6 times in both halves of the tickets.
•	In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides.

An example of a valid winning ticket:
"Cash$$$$$$Ca$$$$$$sh"

An example of a Jackpot winning valid ticket:
"$$$$$$$$$$$$$$$$$$$$"


----------- Input -----------------------------------------


The input will be read from the console.
The input consists of a single line containing all tickets separated by commas and one or more white spaces in the format:
"{ticket}, {ticket}, … {ticket}"


----------- Output ----------------------------------------


Print the result for every ticket in the order of their appearance, each on a separate line in the format:

•	If the ticket is invalid:
"invalid ticket"

•	If the ticket is valid, but it is not winning:
"ticket "{ticket}" - no match"

•	If the ticket is valid and winning, but not a Jackpot: 
"ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"

•	It the ticket hits the Jackpot:
"ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"


------------ Constrains -----------


•	Number of tickets will be in range [0 … 100]


------------ Examples -------------


Input 1:
Cash$$$$$$Ca$$$$$$sh

Output 1:
ticket "Cash$$$$$$Ca$$$$$$sh" - 6$


-----------------------------------


Input 2:
$$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey

Output 2:
ticket "$$$$$$$$$$$$$$$$$$$$" - 10$ Jackpot!
invalid ticket
ticket "th@@@@@@eemo@@@@@@ey" - 6@


-----------------------------------


Input 3:
validticketnomatch:(, Cas$$$$$$$Ca$$$$$$s$

Output 3:
ticket "validticketnomatch:(" - no match
ticket "Cas$$$$$$$Ca$$$$$$s$" - 6$


----------------------------------- 
"""
