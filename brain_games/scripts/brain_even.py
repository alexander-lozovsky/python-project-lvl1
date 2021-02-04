#!/usr/bin/env python

"""brain_even."""

import prompt

from brain_games.cli import welcome_user
from brain_games.games import is_even


def main():
    """Start is even number game."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    win_count = 0
    while win_count < 3:
        (question, answer) = is_even()
        print('Question: ' + str(question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == answer:
            print('Correct!')
            win_count += 1
        else:
            print(
                user_answer +
                ' is wrong answer ;(. Correct answer was ' +
                answer,
            )
            print("Let's try again, " + name + '!')
            return
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
