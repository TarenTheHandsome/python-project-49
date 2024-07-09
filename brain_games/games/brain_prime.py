from random import randint
import math

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = randint(1, 150)
    is_prime = check_is_prime(number)

    correct_answer = 'yes' if is_prime else 'no'
    return str(number), correct_answer


def check_is_prime(number: int) -> bool:
    if number == 1:
        return False
    elif number == 2:
        return True
    elif not number % 2:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if not number % i:
            return False
    else:
        return True
