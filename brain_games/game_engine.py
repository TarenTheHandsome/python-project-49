#!/usr/bin/env python3

def run_game(func, description):
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f"Hello, {name}!")
    counter = 0
    print(description)
    for i in range(3):
        question, correct_answer = func()
        print(f"Question: {question}")
        answer = (input('Your answer: '))
        if answer == correct_answer:
            print("Correct!")
            counter += 1
        else:
            print(f"'{answer}' is wrong answer;"
                  f"(Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")
    return None
