#!/usr/bin/env python3
from brain_games.games import brain_calc
from brain_games.main_file import core_main


def main():
    core_main(brain_calc.find_correct_answer, 'calc')


if __name__ == '__main__':
    main()
