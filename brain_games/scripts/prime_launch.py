#!/usr/bin/env python3
from brain_games.games import brain_prime
from brain_games.game_engine import run_game


def main():
    from brain_games.games.brain_prime import is_prime
    for x in range(1, 155):
        f"{x} is prime: {is_prime(x)}"

    run_game(brain_prime.get_question_and_answer, brain_prime.DESCRIPTION)


if __name__ == '__main__':
    main()
