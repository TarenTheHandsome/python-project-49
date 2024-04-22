#!/usr/bin/env python3
def say_hello():
    print('Welcome to the Brain Games!')
    name = input('May I have your name?')
    print(f"Hello, {name}!")
    return name


def ask_answer(question, flag):
    if flag == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif flag == 'calc':
        print('What is the result of the expression?')
    elif flag == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    elif flag == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    elif flag == 'progression':
        print('What number is missing in the progression?')

    print(f"Question: {question}")
    answer = (input('Your answer: '))
    return answer


def wrong_answer(answer, correct_answer, name):
    print(f"'{answer}' is wrong answer;(Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")
    return None


def say_correct():
    print("Correct!")


def say_congratulations(name):
    print(f"Congratulations, {name}!")


def main(func, flag):
    name = say_hello()
    answers = []
    while len(answers) < 3:
        question, correct_answer = func()
        answer = ask_answer(question, flag)
        if answer == correct_answer:
            answers.append(answer)
            say_correct()
        else:
            wrong_answer(answer, correct_answer, name)
    if len(answers) == 3:
        say_congratulations(name)
    return None

