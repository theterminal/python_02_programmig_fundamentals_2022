# 20220803 - Python - RegEx
# Example!!!


import re

# a string
str_1 = '$$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|'

# split string into chunks
chunks = re.split('#[A-Z][a-z]+[\sA-Z]{,2}[a-z]+#[0-9]{2}[/|.][0-9]{2}[/|.][0-9]{2}#[0-9]{,4}' , str_1)

result_1 = re.findall('#[A-Z][a-z]+[\sA-Z]{,2}[a-z]+#[0-9]{2}[/|.][0-9]{2}[/|.][0-9]{2}#[0-9]{,4}', str_1)
result_2 = re.findall('#([A-Z][a-z]+[\sA-Z]{,2}[a-z]+)#([0-9]{2}[/|.][0-9]{2}[/|.][0-9]{2})#([0-9]{,4})', str_1)
result_3 = re.findall('#([A-Z][a-z]+[\sA-Z]{,2}[a-z]+)#[0-9]{2}[/|.][0-9]{2}[/|.][0-9]{2}#[0-9]{,4}', str_1)
result_4 = re.findall('#[A-Z][a-z]+[\sA-Z]{,2}[a-z]+#([0-9]{2}[/|.][0-9]{2}[/|.][0-9]{2})#[0-9]{,4}', str_1)
result_5 = re.findall('#[A-Z][a-z]+[\sA-Z]{,2}[a-z]+#[0-9]{2}[/|.][0-9]{2}[/|.][0-9]{2}#([0-9]{,4})', str_1)

# print chunks
print(chunks)           # ['$$#@@%^&', '#|', '|$5*(@!', '#^#@aswe|Milk|05/09/20|2000|']

print(result_1)         # ['#Fish#24/12/20#8500', '#Incorrect#19.03.20#450', '#Ice Cream#03/10/21#9000']
print(result_2)         # [('Fish', '24/12/20', '8500'), ('Incorrect', '19.03.20', '450'), ('Ice Cream', '03/10/21', '9000')]
print(result_3)         # ['Fish', 'Incorrect', 'Ice Cream']
print(result_4)         # ['24/12/20', '19.03.20', '03/10/21']
print(result_5)         # ['8500', '450', '9000']


""" Notes 

1) The 'split' method deletes exactly the characters 'findall' returns as a result!
2) The groups defined with '()' in the regex, are the returned result!
3) If you have more than 1 group defined, the result is in the form of tuples, otherwise it is a list!



playground Python IDE:
https://pythonexamples.org/run.php

"""


# --------------------------------------------------
