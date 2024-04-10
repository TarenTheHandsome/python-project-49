#!/usr/bin/env python3
from brain_games.scripts.games.main_file import main
from random import randint


def find_correct_answer():
    num = randint(1, 20)
    if num % 2 == 0:
         correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(num), correct_answer


main(find_correct_answer, 'even')


if __name__ == '__main__':
    main()
