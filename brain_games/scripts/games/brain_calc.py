#!/usr/bin/env python3
from random import randint
from random import choice
from brain_games.scripts.games.say_hello import say_hello


def main():
    answers = []
    name = say_hello()
    while len(answers) < 3:
        a = randint(1, 20)
        b = randint(1, 20)
        operations = {(f"{a} + {b}"):(a + b), (f"{a} - {b}"): (a - b), (f"{a} * {b}"):(a * b)}
        op = choice(list(operations))
        print(f"Question:{op}")
        answer = int(input('Your answer: '))
        if answer == operations[op]:
            answers.append(answer)
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer;(Correct answer was '{operations[op]}'.")
            print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()


