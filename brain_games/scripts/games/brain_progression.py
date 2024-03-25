#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.say_hello import say_hello
from random import choice


def make_progression():
    lenght = randint(5, 10)
    a1 = randint(1, 20)
    d = randint(2, 10)
    result = []
    for i in range(lenght):
        result.append(a1 + i * d)
    return result


def main():
    answers = []
    name = say_hello()
    print('What number is missing in the progression?')
    while len(answers) < 3:
        progression = make_progression()
        num = choice(progression)
        id = progression.index(num)
        progression[id] = '..'
        string = (' '.join(map(str, progression)))
        print(f"Question:{string}")
        answer = int(input('Your answer: '))
        if answer == num:
            answers.append(answer)
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer;(Correct answer was '{num}'.")
            print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
