# 20220608 - Python Code - Functions - Lecture
# 02 - Grades - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#1


# --------------------------- version 1 -------------------------- judge 100%


def grade_test(grade):

    if 2.00 <= grade < 3:
        return 'Fail'
    elif grade < 3.50:
        return 'Poor'
    elif grade < 4.50:
        return 'Good'
    elif grade < 5.50:
        return 'Very Good'
    else:
        return 'Excellent'


entry = float(input())
print(grade_test(entry))


""" ______________ Grades ______________


Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.

•	2.00 – 2.99 - "Fail"
•	3.00 – 3.49 - "Poor"
•	3.50 – 4.49 - "Good"
•	4.50 – 5.49 - "Very Good"
•	5.50 – 6.00 - "Excellent"


____________ Test Data ____________


Input 1:
-------
3.33


Output 1:
--------
Poor


----------------------------------


Input 2:
-------
4.50


Output 2:
--------
Very Good


----------------------------------


Input 3:
-------
2.99


Output 3:
--------
Fail


----------------------------------
"""
