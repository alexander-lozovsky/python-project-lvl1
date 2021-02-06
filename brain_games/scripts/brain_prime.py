#!/usr/bin/env python

"""brain_prime."""

from brain_games.games.prime import prime
from brain_games.run_game import run_game


def main():
    """Run brain-prime game."""
    run_game(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        prime,
    )


if __name__ == '__main__':
    main()
