# 20220529 - Python - Python Fundamentals - L9 - Data Types and Variables
# Notes 08 - Forex Python


from forex_python.converter import CurrencyRates
# must have module 'forex-python' installed via terminal command 'pip install forex-python'


amount = float(input('Enter GBP amount: '))
c = CurrencyRates()
current_rate = c.get_rate('GBP', 'USD')
result = amount * current_rate
print(f'GBP {amount} = USD {result:.3f}')

print(f"EUR / USD = {CurrencyRates().get_rate('EUR', 'USD')}")
print(f"GBP / USD = {(CurrencyRates().get_rate('GBP', 'USD')):.4f}")
print(f"EUR / BGN = {CurrencyRates().get_rate('EUR', 'BGN')}")
print(f"USD / BGN = {(CurrencyRates().get_rate('USD', 'BGN')):.4f}")

