#!/usr/bin/env python3
from brain_games.games import brain_calc
from brain_games.game_engine import run_game


def main():
    run_game(brain_calc.find_correct_answer, brain_calc.description)


if __name__ == '__main__':
    main()
