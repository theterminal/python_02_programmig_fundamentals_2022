# 20220722 - Python Code - Regular Expressions - Exercise
# 03 - Find Occurrences of Word in Sentence - judge url: https://judge.softuni.org/Contests/Compete/Index/1743#2

import re
# use this to construct the regex: https://regex101.com/


# ------------------------ version 1 -------------------- judge: 100%


sentence = input()
searched_word = input()
pattern = fr'\b{searched_word}\b'
matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
print(len(matches))
