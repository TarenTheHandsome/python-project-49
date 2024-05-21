#!/usr/bin/env python3
from random import randint
from brain_games.main_file import core_main
from random import choice


# def main():
#     core_main(find_correct_answer, 'progression')


def find_correct_answer():
    length = randint(5, 10)
    a1 = randint(1, 20)
    d = randint(2, 10)
    progression = []
    for i in range(length):
        progression.append(a1 + i * d)
    num = choice(progression)
    my_id = progression.index(num)
    progression[my_id] = '..'
    progression_string = (' '.join(map(str, progression)))
    return progression_string, str(num)


# if __name__ == '__main__':
#     main()
