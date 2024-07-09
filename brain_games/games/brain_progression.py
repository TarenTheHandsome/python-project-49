from random import randint
from random import choice

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(1, 20)
    step = randint(2, 8)
    stop = start + step * randint(5, 10)
    progression = list(range(start, stop, step))
    num = choice(progression)
    my_id = progression.index(num)
    progression[my_id] = '..'
    progression_string = (' '.join(map(str, progression)))
    return progression_string, str(num)
