#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.say_hello import say_hello


# def say_hello():
#     print('Welcome to the Brain Games!')
#     name = input('May I have your name? ')
#     print(f"Hello, {name}!")
#     print('Answer "yes" if the number is even, otherwise answer "no".')
#     return name


def check_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    answers = []
    name = say_hello()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while len(answers) < 3:
        num = randint(1, 20)
        print(f"Question: {num}")
        answer = input('Your answer: ')
        right_answer = check_even(num)
        if answer == right_answer:
            answers.append(answer)
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer;(Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()

