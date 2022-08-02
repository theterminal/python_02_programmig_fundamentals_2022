# 20220529 - Python - Python Fundamentals - L08 - Data Types and Variables
# 05 - Pounds to Dollars - judge url: https://judge.softuni.org/Contests/Practice/Index/1721#4


# ------------- version 1 ----------------------- judge: 100%


gbp_entered_to_convert_to_usd = int(input())
gbp_to_usd_rate = 1.31

usd = gbp_entered_to_convert_to_usd * gbp_to_usd_rate
print(f'{usd:.3f}')


""" -------------------- Pounds to Dollars --------------------


Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
1 British Pound = 1.31 Dollars.


---------- Test Data -------------


Input 1:                Output 1:
-------                 --------
80                      104.800


----------------------------------


Input 2:                Output 2:
-------                 --------
39                      51.090


----------------------------------


"""
