#!/usr/bin/env python3
from random import randint
from random import choice

description = 'What is the result of the expression?'


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
