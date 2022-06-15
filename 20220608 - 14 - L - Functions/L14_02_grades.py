# 20220608 - Python Code - Functions - Lecture
# 02 - Grades - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#1


def grade_test(grade):
    result = None

    if 2.00 <= grade < 3:
        result = 'Fail'
    elif grade < 3.50:
        result = 'Poor'
    elif grade < 4.50:
        result = 'Good'
    elif grade < 5.50:
        result = 'Very Good'
    else:
        result = 'Excellent'

    return result


entry = float(input())
print(grade_test(entry))
