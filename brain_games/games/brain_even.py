#!/usr/bin/env python3
from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def find_correct_answer():
    num = randint(1, 20)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(num), correct_answer
