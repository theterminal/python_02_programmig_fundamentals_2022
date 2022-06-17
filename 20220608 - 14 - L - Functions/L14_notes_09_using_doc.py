# 20220608 - Python Code - Functions - Lecture
# 09 - Using __doc__


# -------- using __doc__ --------------------


def name_f():
    """

    :return: This is a test text to demonstrate the '__doc__' functionality
    """

    return 'Some results'


print(name_f())
print(name_f.__doc__)

