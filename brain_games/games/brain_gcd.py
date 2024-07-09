from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    a = randint(20, 200)
    b = randint(20, 200)
    return str(f'{a} {b}'), str(gcd(a, b))
