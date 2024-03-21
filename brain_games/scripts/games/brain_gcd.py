#!/usr/bin/env python3
from random import randint
from math import gcd
from brain_games.scripts.games.say_hello import say_hello


def create_nums():
    a = randint(1, 200)
    b = randint(1, 200)
    return a, b


def check():
    a, b = create_nums()
    while gcd(a, b) == 1:
        a, b = create_nums()
    return a, b, gcd(a, b)



def main():
    answers = []
    name = say_hello()
    print('Find the greatest common divisor of given numbers.')
    while len(answers) < 3:
        a, b, nod = check()
        print(f"Question: {a} {b}")
        answer = int(input('Your answer: '))
        if answer == nod:
            answers.append(answer)
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer;(Correct answer was '{nod}'.")
            print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
