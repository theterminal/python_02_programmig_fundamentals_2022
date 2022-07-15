# 20220629 - Python Code - Objects and Classes - Lecture
# 03 - Email - judge url: https://judge.softuni.org/Contests/Practice/Index/1733#2


# ----------------------- version 3 --------------------------------


class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []

while True:
    command = input()
    if command == 'Stop':
        break

    token_sender, token_receiver, token_content = command.split(' ')
    email = Email(token_sender, token_receiver, token_content)
    emails.append(email)

send_emails = [emails[int(x)].send() for x in input().split(', ')]

for email in emails:
    print(email.get_info())


# ----------------------- version 2 --------------------------------


class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []

while True:
    command = input()
    if command == 'Stop':
        break

    token_sender, token_receiver, token_content = command.split(' ')
    email = Email(token_sender, token_receiver, token_content)
    emails.append(email)

send_emails = list(map(lambda x: int(x), input().split(', ')))
# send_emails = list(map(int, input().split(', ')))                        # if not using lambda

for index in send_emails:
    emails[index].send()

for email in emails:
    print(email.get_info())


# ----------------------- version 1 --------------------------------


class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []

while True:
    command = input()
    if command == 'Stop':
        break

    tokens = command.split(' ')
    token_sender = tokens[0]
    token_receiver = tokens[1]
    token_content = tokens[2]
    email = Email(token_sender, token_receiver, token_content)
    emails.append(email)

send_emails = list(map(lambda x: int(x), input().split(', ')))

for i in send_emails:
    emails[i].send()

for email in emails:
    print(email.get_info())
