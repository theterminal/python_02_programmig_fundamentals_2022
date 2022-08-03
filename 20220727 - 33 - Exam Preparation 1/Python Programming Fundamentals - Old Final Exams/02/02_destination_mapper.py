# 20220803 - Python Code - Exam Preparation
# 02 - Destination Mapper - judge url: https://judge.softuni.org/Contests/Practice/Index/2518#1

import re


# ------------------------- version 1 ------------------------ judge: 100%


def string_validation(string):
    pattern = r'\={1}[A-Z]{1}[A-za-z]{2,}\={1}|\/{1}[A-Z]{1}[A-za-z]{2,}\/{1}'
    valid_string = re.findall(pattern, string)
    valid = []

    for el in valid_string:
        sign = el[0]
        valid_el = el.strip(sign)
        valid.append(valid_el)
    return valid


def output(valid):
    print(f"Destinations: {', '.join(valid)}")
    total_len = 0
    for element in valid:
        total_len += len(element)
    print(f"Travel Points: {total_len}")


def destination_mapper():
    string_in = input()

    valid_string = string_validation(string_in)
    output(valid_string)


destination_mapper()


""" ---------------- Destination Mapper -------------------


Now that you have planned out your tour, you are ready to go!
Your next task is to mark all the points on the map that you are going to visit.

You will be given a string representing some places on the map.
You have to filter only the valid ones.

A valid location is:
    •	Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
    •	After the first "=" or "/" there should be only letters (the first must be upper-case, other letters could be upper or lower-case)
    •	The letters must be at least 3

Example:
-------
In the string:

"=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i="

only the first two locations are valid.

After you have matched all the valid locations, you have to calculate travel points.
They are calculated by summing the lengths of all the valid destinations that you have found on the map. 

In the end, on the first line, print:

"Destinations: {destinations joined by ', '}".

On the second line, print:

"Travel Points: {travel_points}".


Input / Constraints:
-------------------
    •	You will receive a string representing the locations on the map
    •	JavaScript: you will receive a single parameter: string

Output:
------
    •	Print the messages described above
    
    
--------------- Test Data -----------------


Input 1:
-------
=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=


Output 1:
--------
Destinations: Hawai, Cyprus
Travel Points: 11


-------------------------------------------


Input 2:
-------
ThisIs some InvalidInput


Output 2:
--------
Destinations:
Travel Points: 0


-------------------------------------------

"""