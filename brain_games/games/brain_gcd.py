#!/usr/bin/env python3
from random import randint
from math import gcd

description = 'Find the greatest common divisor of given numbers.'


def create_nums():
    a = randint(1, 200)
    b = randint(1, 200)
    return a, b


def find_correct_answer():
    a, b = create_nums()
    while gcd(a, b) == 1:
        a, b = create_nums()
    return str(f'{a} {b}'), str(gcd(a, b))
