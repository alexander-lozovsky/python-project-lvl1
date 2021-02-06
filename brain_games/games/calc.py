"""Games."""
from random import randint

OPERAND_MIN = 1
OPERAND_MAX = 30
PLUS_CODE = 1
MINUS_CODE = 2
MULTIPLY_CODE = 3


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
    operator_code = randint(1, 3)

    if operator_code == PLUS_CODE:
        question = f'{left_operand} + {right_operand}'
        answer = str(left_operand + right_operand)

        return (question, answer)
    if operator_code == MINUS_CODE:
        question = f'{left_operand} - {right_operand}'
        answer = str(left_operand - right_operand)

        return (question, answer)
    if operator_code == MULTIPLY_CODE:
        question = f'{left_operand} * {right_operand}'
        answer = str(left_operand * right_operand)

        return (question, answer)
