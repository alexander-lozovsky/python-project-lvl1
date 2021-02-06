"""Game engine."""
import prompt

from brain_games.cli import ask_user_name, welcome_user


def run_game(rules, game):
    """
    Run game engine.

    Parameters:
        rules: game rules, will be displayed to the user at the beginning.
        game: (question, answer) tuple.
    """
    welcome_user()
    name = ask_user_name()
    print(rules)

    win_count = 0
    while win_count < 3:
        (question, answer) = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == answer:
            print('Correct!')
            win_count += 1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {answer}.')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
