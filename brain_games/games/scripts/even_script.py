#!/usr/bin/env python3
from brain_games.games import brain_even
from brain_games.main_file import core_main


def main():
    core_main(brain_even.find_correct_answer, 'even')


if __name__ == '__main__':
    main()
