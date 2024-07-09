from random import randint
from random import choice
import operator

DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    a = randint(1, 20)
    b = randint(1, 20)
    operations = [
        ('-', operator.sub(a, b)),
        ('+', operator.add(a, b)),
        ('*', operator.mul(a, b))
    ]
    op, correct_answer = choice(operations)
    return f'{a} {op} {b}', str(correct_answer)
