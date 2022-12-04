# 20220608 - Python - Functions - Lecture
# 02 - Creating and Invoking a Functions


# --------------------- example 1 ----------------


def print_header():
    print('\nPrinted from the function')


print_header()


# --------------------- example 2 ----------------


def print_footer():
    print('This is the footer of page!\n')


def display_page():
    print_header()
    print_footer()


display_page()


# ---------------------- recursion ---------------


def crash():
    crash()


# crash()
