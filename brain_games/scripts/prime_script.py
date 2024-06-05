#!/usr/bin/env python3
from brain_games.games import brain_prime
from brain_games.game_engine import run_game


def main():
    run_game(brain_prime.find_correct_answer, brain_prime.description)


if __name__ == '__main__':
    main()
