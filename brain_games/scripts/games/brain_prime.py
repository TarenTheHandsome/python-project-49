#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.main_file import main


def find_correct_answer():
    prime_ints = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
    new_int = randint(1, 150)
    if new_int in prime_ints:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(new_int), correct_answer


if __name__ == '__main__':
    main(find_correct_answer, 'prime')
