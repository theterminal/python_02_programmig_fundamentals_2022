# 20220601 - Python Code - L11 - Lists - Basics
# 01 - Strange Zoo - judge url: https://judge.softuni.org/Contests/Practice/Index/1724#0

# str_tail = input()
# str_body = input()
# str_head = input()
#
# animal = [str_head, str_body, str_tail]
#
# print(animal)

# ------------- switching elements in a list ------------

test_animal = [input(), input(), input()]
print(test_animal)

test_animal[0], test_animal[-1] = test_animal[-1], test_animal[0]
print(test_animal)

# -------------------------------------------------------
