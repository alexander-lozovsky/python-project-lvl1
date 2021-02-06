#!/usr/bin/env python

"""brain_progression."""

from brain_games.games.progression import progression
from brain_games.run_game import run_game


def main():
    """Run brain-progression game."""
    run_game(
        'What number is missing in the progression?',
        progression,
    )


if __name__ == '__main__':
    main()
