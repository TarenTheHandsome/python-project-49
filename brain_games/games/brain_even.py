from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    num = randint(1, 20)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return str(num), correct_answer


