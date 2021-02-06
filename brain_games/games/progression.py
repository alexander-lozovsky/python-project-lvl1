"""Progression game."""
from random import randint

MIN_NUMBER = 0
MAX_NUMBER = 20
MAX_STEP = 5
MIN_LENGTH = 5
MAX_LENGTH = 10


def progression():  # noqa: WPS210
    """
    Generate progression game .

    Returns:
        (question, answer) tuple:
            - question - progression from 5 to 10 numbers with a gap
            - answer - a gap in the given progression
    """
    start = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(1, MAX_STEP)
    length = randint(MIN_LENGTH, MAX_LENGTH)
    gap = randint(0, length - 1)
    question = []
    index = 0

    while index < length:
        if index == gap:
            question.append('..')
        else:
            question.append(str(start + (step * index)))

        index += 1

    return (' '.join(question), str(start + (step * gap)))
