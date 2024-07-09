from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


# def create_nums():
#     a = randint(1, 200)
#     b = randint(1, 200)
#     return a, b
#
#
# def get_question_and_answer():
#     a, b = create_nums()
#     while gcd(a, b) == 1:
#         a, b = create_nums()
#     return str(f'{a} {b}'), str(gcd(a, b))

def get_question_and_answer():
    a = randint(20, 200)
    b = randint(20, 200)
    return str(f'{a} {b}'), str(gcd(a, b))


