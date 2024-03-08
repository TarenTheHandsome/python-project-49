#!/usr/bin/env python3
from ..cli import welcome_user
import prompt

def print_welcome():
    print('Welcome to the Brain Games!')
    welcome_user()


def main():
    print_welcome()


if __name__ == '__main__':
    main()
