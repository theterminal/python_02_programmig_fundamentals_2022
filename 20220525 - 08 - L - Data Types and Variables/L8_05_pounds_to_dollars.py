# 20220529 - Python - Python Fundamentals - L9 - Data Types and Variables
# 05 - Pounds to Dollars - judge url: https://judge.softuni.org/Contests/Practice/Index/1721#4


gbp_entered_to_convert_to_usd = int(input())
gbp_to_usd_rate = 1.31

usd = gbp_entered_to_convert_to_usd * gbp_to_usd_rate
print(f'{usd:.3f}')
