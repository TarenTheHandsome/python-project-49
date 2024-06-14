#!/usr/bin/env python3
from brain_games.games import brain_even
from brain_games.game_engine import run_game


def main():
    run_game(brain_even.get_question_and_answer, brain_even.DESCRIPTION)


if __name__ == '__main__':
    main()
