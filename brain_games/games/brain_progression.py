from random import randint
from random import choice

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
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
