"""cli."""

import prompt


def welcome_user():
    """Show greeting."""
    print('Welcome to the Brain Games!')


def ask_user_name():
    """
    Ask user name.

    Returns:
        user name
    """
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    return name
