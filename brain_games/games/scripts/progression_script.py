#!/usr/bin/env python3
from brain_games.games import brain_progression
from brain_games.main_file import core_main


def main():
    core_main(brain_progression.find_correct_answer, 'progression')


if __name__ == '__main__':
    main()
