# 20220722 - Python Code - Regular Expressions - Exercise
# 04 - Extract Emails - judge url: https://judge.softuni.org/Contests/Compete/Index/1743#3

import re
# use this to construct the regex: https://regex101.com/


# ------------------------ version 1 -------------------- judge: 100%

string = input()

pattern = r'(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'
matches = re.findall(pattern, string)
# print(matches[0][0])

for element in matches:
    print(element[0])


"""


Write a program that receives a single string and extracts all email addresses from it.
Print the extracted email addresses on separate lines.
Emails are in the format "{user}@{host}", where:

•	{user} -    could consist only of letters and digits; the symbols ".", "-" and "_" can appear between them.

    o	Examples of valid users: "stephan", "mike03", "s.johnson", "st_steward", "softuni-bulgaria", "12345"
    o	Examples of invalid users: ''--123", ".....", "nakov_-", "_steve", ".info"

•	{host}  -   is a sequence of at least two words, each couple of words must be separated by a single dot ".".
                Each word consists of only letters and can have hyphens "-" between the letters.
                
    o	Examples of valid hosts: "softuni.bg", "software-university.com", "intoprogramming.info", "mail.softuni.org"
    o	Examples of invalid hosts: "helloworld", ".unknown.soft." , "invalid-host-", "invalid-"


Examples of valid emails:
-------------------------
    *) info@softuni-bulgaria.org
    *) kiki@hotmail.co.uk
    *) no-reply@github.com
    *) s.peterson@mail.uu.net
    *) info-bg@software-university.software.academy

Examples of invalid emails:
---------------------------
    *) --123@gmail.com
    *) …@mail.bg
    *) .info@info.info
    *) _steve@yahoo.cn
    *) mike@helloworld
    *) mike@.unknown.soft.
    *) s.johnson@invalid-


--------------- Examples -------------------


Input 1:
--------
Please contact us at: support@github.com.


Output 1:
---------
support@github.com


--------------------------------------------


Input 2:
--------
Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.


Output 2:
s.miller@mit.edu
j.hopking@york.ac.uk


--------------------------------------------


Input 3:
--------
Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class. –- steve.parker@softuni.de.


Output 3:
---------
steve.parker@softuni.de


"""
