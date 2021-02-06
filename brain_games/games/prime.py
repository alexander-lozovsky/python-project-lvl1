"""Is prime number game."""
from random import randint


def prime():
    """
    Generate is prime number game.

    Returns:
        (question, answer) tuple:
            - question - random number
            - answer - "yes" or "no"
    """
    question = randint(2, 100)
    answer = 'yes'

    counter = question // 2
    while counter > 1:
        if question % counter == 0:
            answer = 'no'
            break
        counter -= 1

    return (str(question), answer)
