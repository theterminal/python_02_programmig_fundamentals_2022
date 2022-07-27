# 20220722 - Python Code - Regular Expressions - Lecture
# 03 - Match Dates - judge url: https://judge.softuni.org/Contests/Practice/Index/1742#2

import re
# use this to construct the regex: https://regex101.com/


# ------------------------ version 1 -------------------- judge: 100%


dates = input()
regex = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'                  # '\2' means: match the found separator from group 2 for this group also!

result = re.findall(regex, dates)

for match in result:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')


""" -------------- Comments -----------------------------


* - We'll create 5 groups       ()()()()()
    - 1-st is the date          (\d{2})             - find group of 2 digits
    - 2-nd is the separator     ([\/.-])            - find separator '/' or '.' or '-'
    - 3-d is the month          ([A-Z][a-z]{2})     - find 3 letter word with 1 Cap Letter and 2 small
    - 4-th is the separator     \2                  - find separator that matches the separator from group 2!!! (back-reference)
    - 5-th is the year          (\d{4})             - find group of 4 digits 


"""


""" -------------------- Match Dates ---------------------


Write a program, which matches a date in the format:

"dd{separator}MMM{separator}yyyy".

Use capturing groups in your regular expression.


Compose the Regular Expression:

Every valid date has the following characteristics:
•	It always starts with two digits, followed by a separator.
•	After that, it has one uppercase and two lowercase letters (e.g., Jan, Mar).
•	After that, it has a separator and exactly 4 digits (for the year).
•	The separator could be one of these symbols: a period ("."), a hyphen ("-") or a forward-slash ("/").
•	The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT). Use a group back-reference to check for this.


Input 1:
--------

13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016


Output 1:
---------

Day: 13, Month: Jul, Year: 1928
Day: 10, Month: Nov, Year: 1934
Day: 25, Month: Dec, Year: 1937


"""