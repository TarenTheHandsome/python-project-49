import prompt


def run_game(do_math, description):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    iteration = 3
    print(description)
    for _ in range(iteration):
        question, correct_answer = do_math()
        print(f"Question: {question}")
        answer = (input('Your answer: '))
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer;"
                  f"(Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
