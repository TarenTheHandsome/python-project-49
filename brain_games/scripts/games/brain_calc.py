#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.main_file import core_main
from random import choice


def main():
    core_main(find_correct_answer, 'calc')


def find_correct_answer():
    a = randint(1, 20)
    b = randint(1, 20)
    operations = {
        (f"{a} + {b}"): (a + b),
        (f"{a} - {b}"): (a - b),
        (f"{a} * {b}"): (a * b)}
    op = choice(list(operations))
    correct_answer = operations[op]
    return op, str(correct_answer)


if __name__ == '__main__':
    main()
