# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 04 - Maximum Multiple - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#3


divisor = int(input())
boundary = int(input())
max_multiplier = 0

for current_num in range(boundary, divisor, -1):
    if current_num % divisor == 0:
        max_multiplier = current_num
        print(max_multiplier)
        break

# ---------------------------------------------------
# # interesting concept from Юри Димитров

divisor = int(input())
boundary = int(input())

print((boundary // divisor) * divisor)
