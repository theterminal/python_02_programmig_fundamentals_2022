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


""" ---------------- Find Occurrences of Word in Sentence -------------


Write a program that finds how many times a word is used in a string.
The output is a single number indicating the number of times the string contains the word.
Note that letter case does not matter – it is case-insensitive.


------------------ Examples -------------------

Input 1:
--------
The waterfall was so high, that the child couldn't see its peak.
the


Output 1:
---------
2


-------------------------------------------------


Input 2:
--------
How do you plan on achieving that? How? How can you even think of that? 
how

Output 2:
--------
3


-------------------------------------------------


Input 3:
--------
There was one. Therefore I bought it. I wouldn't buy it otherwise.
there


Output 3:
---------
1


"""