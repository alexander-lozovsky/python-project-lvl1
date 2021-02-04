"""Games."""
from random import randint


def is_even():
    """Is even number game."""
    question = randint(1, 100)
    answer = ''

    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return (question, answer)
