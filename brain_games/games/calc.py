"""Games."""
from random import randint

OPERAND_MIN = 1
OPERAND_MAX = 30
PLUS_CODE = 1
MINUS_CODE = 2
MULTIPLY_CODE = 3


def generate_question(left, right, operator):
    """
    Generate question string.

    Parameters:
        left: left operand
        right: right operand
        operator: operator

    Returns:
        question with format like: "15 + 16"
    """
    return str(left) + ' ' + operator + ' ' + str(right)


def calc():
    """
    Generate calculate ab expression game.

    Returns:
        (question, answer) tuple:
            - question - random expression
            - answer - expression result
    """
    left_operand = randint(OPERAND_MIN, OPERAND_MAX)
    right_operand = randint(OPERAND_MIN, OPERAND_MAX)
    operator = randint(1, 3)

    if operator == PLUS_CODE:
        question = generate_question(left_operand, right_operand, '+')
        answer = str(left_operand + right_operand)

        return (question, answer)
    if operator == MINUS_CODE:
        question = generate_question(left_operand, right_operand, '-')
        answer = str(left_operand - right_operand)

        return (question, answer)
    if operator == MULTIPLY_CODE:
        question = generate_question(left_operand, right_operand, '*')
        answer = str(left_operand * right_operand)

        return (question, answer)
