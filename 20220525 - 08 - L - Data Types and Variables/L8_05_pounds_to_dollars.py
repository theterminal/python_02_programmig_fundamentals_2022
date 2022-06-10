# 20220529 - Python - Python Fundamentals - L9 - Data Types and Variables
# 05 - Pounds to Dollars - judge url: https://judge.softuni.org/Contests/Practice/Index/1721#4

from forex_python.converter import CurrencyRates
# must have module 'forex-python' installed via terminal command 'pip install forex-python'

# ----------------- version 1 ------------------ passes judge 100%

gbp_entered_to_convert_to_usd = int(input())
gbp_to_usd_rate = 1.31

usd = gbp_entered_to_convert_to_usd * gbp_to_usd_rate
print(f'{usd:.3f}')

# ----------------- version 2 ----------------- not for judge system

amount = float(input('Enter GBP amount: '))
c = CurrencyRates()
current_rate = c.get_rate('GBP', 'USD')
result = amount * current_rate
print(f'GBP {amount} = USD {result:.3f}')

print(f"EUR / USD = {CurrencyRates().get_rate('EUR', 'USD')}")
print(f"GBP / USD = {(CurrencyRates().get_rate('GBP', 'USD')):.4f}")
print(f"EUR / BGN = {CurrencyRates().get_rate('EUR', 'BGN')}")
print(f"USD / BGN = {(CurrencyRates().get_rate('USD', 'BGN')):.4f}")

