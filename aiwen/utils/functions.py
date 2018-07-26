import random


def get_ticket():
    s = '1234567890qwertyuiopasdfghjklzxcvbnm'

    ticket = ''
    for i in range(28):
        a = random.choice(s)
        ticket += a
    return ticket


