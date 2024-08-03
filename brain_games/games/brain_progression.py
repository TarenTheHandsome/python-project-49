import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(1, 20)
    step = random.randint(2, 8)
    length_of_pg = start + step * random.randint(5, 10)
    progression = list(range(start, length_of_pg, step))
    hidden_index = random.randrange(len(progression))
    answer = progression[hidden_index]
    progression[hidden_index] = '..'
    progression_string = (' '.join(map(str, progression)))
    return progression_string, str(answer)
