# 20220608 - Python - Functions - Lecture
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
