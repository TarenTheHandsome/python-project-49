import prompt


def run_game(get_question_and_answer, description):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    game_rounds = 3
    print(description)

    for _ in range(game_rounds):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        answer = (input('Your answer: '))

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer;"
                  f"(Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")

    print(f"Congratulations, {name}!")
