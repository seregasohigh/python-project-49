#!/usr/bin/env python3
from brain_games import cli


def welcome():
    print('Welcome to the Brain Games!')


def main():
    welcome()
    print(cli.welcome_user())


if __name__ == '__main__':
    main()
