"""Is even number game."""
import math
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 30


def gcd():
    """
    Generate gcd game .

    Returns:
        (question, answer) tuple:
            - question - two random numbers
            - answer - the greatest common divisor
    """
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)

    question = str(first_number) + ' ' + str(second_number)
    answer = str(math.gcd(first_number, second_number))

    return (question, answer)
