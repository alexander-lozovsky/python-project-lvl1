"""Is even number game."""
from random import randint


def is_even():
    """
    Generate is even number game.

    Returns:
        (question, answer) tuple:
            - question - random number
            - answer - "yes" or "no"
    """
    question = randint(1, 100)
    answer = ''

    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return (question, answer)
