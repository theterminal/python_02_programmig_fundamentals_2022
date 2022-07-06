# 20220616 - Python Code - Lists Advance - Lecture
# 01 - No Vowels - judge: https://judge.softuni.org/Contests/Practice/Index/1730#0


str_in = input()

nots = ['a', 'o', 'u', 'e', 'i']
result = [i for i in str_in if i.lower() not in nots]

print(''.join(result))
