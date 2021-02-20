#!/usr/bin/env python3

"""brain_calc."""

from brain_games.games.calc import calc
from brain_games.run_game import run_game


def main():
    """Run brain-calc game."""
    run_game('What is the result of the expression?', calc)


if __name__ == '__main__':
    main()
