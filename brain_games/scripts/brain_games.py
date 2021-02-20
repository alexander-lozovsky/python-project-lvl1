#! usr/bin/env python3

"""brain_games."""
from brain_games.cli import ask_user_name, welcome_user


def main():
    """Run greetings."""
    welcome_user()
    ask_user_name()


if __name__ == '__main__':
    main()
