# 20220601 - Python Code - L11 - Lists - Basics
# 01 - Strange Zoo - judge url: https://judge.softuni.org/Contests/Practice/Index/1724#0


# --------------------- version 1 -------------------------- judge 100%


str_tail = input()
str_body = input()
str_head = input()

animal = [str_head, str_body, str_tail]

print(animal)


# ------------- switching elements in a list ------------


test_animal = [input(), input(), input()]
print(test_animal)

test_animal[0], test_animal[-1] = test_animal[-1], test_animal[0]
print(test_animal)


""" --------------- Strange Zoo ----------------


You are at the zoo, and the meerkats look strange. 

You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order.
Your task is to re-arrange the elements in a list so that the animal looks normal again:
    •	On the first position is the head;
    •	On the second position is the body;
    •	On the last one is the tail.


----------- Test Data -------------


Input 1:
-------
my tail
my body seems on place
my head is on the wrong end!


Output 1:
--------
['my head is on the wrong end!', 'my body seems on place', 'my tail']


-----------------------------------


Input 2:
-------
tail
body
head


Output 2:
--------
['head', 'body', 'tail']


-----------------------------------


Input 3:
-------
T
B
H


Output 3:
--------
['H', 'B', 'T']


-----------------------------------

"""
