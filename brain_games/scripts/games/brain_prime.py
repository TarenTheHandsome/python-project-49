#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.say_hello import say_hello


def main():
    answers = []
    name = say_hello()
    prime_ints = [2, 3,	5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while len(answers) < 3:
        a = randint(1, 150)
        if a in prime_ints:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f"Question: {a}")
        answer = (input('Your answer: '))
        if answer == correct_answer:
            answers.append(answer)
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer;(Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()