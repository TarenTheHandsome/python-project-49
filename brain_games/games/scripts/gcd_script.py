#!/usr/bin/env python3
from brain_games.games import brain_gcd
from brain_games.main_file import core_main


def main():
    core_main(brain_gcd.find_correct_answer, 'gcd')


if __name__ == '__main__':
    main()
