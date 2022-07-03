# 20220608 - Python Code - Functions - Lecture
# 01 - Absolute Values - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#0


# ---------------- no function ---------------------


str_entered = input().split()
lst_from_str_entered_to_abs_num = [abs(float(i)) for i in str_entered]

print(lst_from_str_entered_to_abs_num)


# ---------------- with function ---------------------


def absolute(nums):
    return [abs(i) for i in nums]


nums_entered = list(map(float, input().split(' ')))
print(absolute(nums_entered))
