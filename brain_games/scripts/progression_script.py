#!/usr/bin/env python3
from brain_games.games import brain_progression
from brain_games.game_engine import run_game


def main():
    run_game(brain_progression.get_question_and_answer,
             brain_progression.DESCRIPTION)


if __name__ == '__main__':
    main()
