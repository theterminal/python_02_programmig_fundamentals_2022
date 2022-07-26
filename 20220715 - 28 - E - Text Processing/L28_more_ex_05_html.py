# 20220721 - Python Code - String Processing - Exercise
# More Exercise 05 - HTML - judge url: https://judge.softuni.org/Contests/Practice/Index/1741#4


# ---------------------- version 1 ----------------------------- judge: 100%


title = input()
print(f'<h1>\n    {title}\n</h1>')

article = input()
print(f'<article>\n    {article}\n</article>')


while True:
    comment = input()
    if comment == 'end of comments':
        break
    print(f'<div>\n    {comment}\n</div>')
