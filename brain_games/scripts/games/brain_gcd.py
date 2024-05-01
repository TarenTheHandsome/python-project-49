#!/usr/bin/env python3
from brain_games.scripts.games.main_file import core_main
from random import randint
from math import gcd


def main():
    core_main(find_correct_answer, 'gcd')


def create_nums():
    a = randint(1, 200)
    b = randint(1, 200)
    return a, b


def find_correct_answer():
    a, b = create_nums()
    while gcd(a, b) == 1:
        a, b = create_nums()
    return str(f'{a} {b}'), str(gcd(a, b))


if __name__ == '__main__':
    main()
