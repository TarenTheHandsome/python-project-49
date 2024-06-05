#!/usr/bin/env python3
from brain_games.games import brain_gcd
from brain_games.game_engine import run_game


def main():
    run_game(brain_gcd.find_correct_answer, brain_gcd.description)


if __name__ == '__main__':
    main()
