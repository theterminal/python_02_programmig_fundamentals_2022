# 20220629 - Python - Objects and Classes - Lecture
# 01 - Comments - judge url: https://judge.softuni.org/Contests/Practice/Index/1733#0


# ---------------- version 1 --------------------- judge 100%


class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)
