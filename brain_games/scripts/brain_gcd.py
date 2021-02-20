#! usr/bin/env python3

"""brain_gcd."""

from brain_games.games.gcd import gcd
from brain_games.run_game import run_game


def main():
    """Run brain-gcd game."""
    run_game(
        'Find the greatest common divisor of given numbers.',
        gcd,
    )


if __name__ == '__main__':
    main()
