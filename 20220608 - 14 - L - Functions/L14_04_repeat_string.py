# 20220614 - Python Code - Functions - Lecture
# 04 - Repeat String - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#3


# ------- normal function --------------------- judge 100%


def repeat_string(str_a1, counter_a2):
    result = str_a1 * counter_a2

    return result


a1 = input()
a2 = int(input())

print(repeat_string(a1, a2))


# ------- using lambda function ---------------- judge 100%


x1 = input()
counter_y = int(input())

result_2 = lambda x, y: x * y
print(result_2(x1, counter_y))


""" ___________________ Repeat String ___________________


Write a function that receives a string and a counter 'n'.
The function should return a new string – the result of repeating the old string 'n' times.

Print the result of the function.
Try using lambda.


____________ Test Data ____________


Input 1:
-------
abc
3


Output 1:
--------
abcabcabc


-----------------------------------


Input 2:
-------
String
2


Output 2:
--------
StringString


----------------------------------
"""
