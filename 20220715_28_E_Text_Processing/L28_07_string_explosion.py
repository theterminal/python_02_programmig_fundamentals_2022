# 20220715 - Python Code - String Processing - Exercise
# 07 - String Explosion - judge url: https://judge.softuni.org/Contests/Compete/Index/1740#6


# ------------------------ version 1 -------------------- judge: 100%


data_in = input()
data = [n for n in data_in]
strength = 0
data_out = []
last_element = ''

for i in range(len(data)):

    if strength > 0:
        if data[i] != '>':
            strength -= 1
            continue

    if data[i] == '>':
        data_out.append(data[i])
        strength += int(data[i + 1])
    else:
        data_out.append(data[i])

print(''.join(data_out))


""" ------------------- String Explosion --------------------------------


Write a program that reads a string from the console that contains:

•	Explosions marked with '>'
•	Immediately after the mark, there will be an 'integer x', which signifies the strength of the explosion
•	Any other characters

Your task is to delete 'x' characters, starting after the exploded character ('>').
If you find another explosion mark ('>') while deleting characters, you should add the strength to your previous explosion.
You should not delete the explosion character – '>'.
When all characters are processed, print the final string. 

Constraints:

•	You will always receive strength for the explosions
•	The path will consist only of letters from the Latin alphabet, integers, and the char '>'
•	The strength of the punches will be in the interval [0…9]


______________________ Examples: ______________________________________________


Input 1:
--------
abv>1>1>2>2asdasd                                   


Output 1:
---------
abv>>>>dasd


-----------------------------------


Input 2:
pesho>2sis>1a>2akarate>4hexmaster


Output 2:
--------
pesho>is>a>karate>master


-----------------------------------


Input 3:
--------
This>7sevenais>4wtfthe>5killcorrect>4kalanswer


Output 3:
---------
This>is>the>correct>answer


"""