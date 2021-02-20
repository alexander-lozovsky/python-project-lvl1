#!/usr/bin/env python3

"""brain_even."""

from brain_games.games.is_even import is_even
from brain_games.run_game import run_game


def main():
    """Run brain-even game."""
    run_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        is_even,
    )


if __name__ == '__main__':
    main()
