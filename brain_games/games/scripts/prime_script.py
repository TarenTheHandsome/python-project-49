#!/usr/bin/env python3
from brain_games.games import brain_prime
from brain_games.main_file import core_main


def main():
    core_main(brain_prime.find_correct_answer, 'prime')


if __name__ == '__main__':
    main()
