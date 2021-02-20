#! usr/bin/env python3

"""brain_games."""
from brain_games.cli import welcome_user, ask_user_name


def main():
    """Run greetings."""
    welcome_user()
    ask_user_name()

if __name__ == '__main__':
    main()
