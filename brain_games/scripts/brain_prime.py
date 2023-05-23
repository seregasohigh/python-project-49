#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def prime_num(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def true_answer(num):
    if prime_num(num):
        return 'yes'
    else:
        return 'no'


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        num = random.randint(1, 100)
        print(f'Question: {num}')
        correct_answer_str = true_answer(num)
        answer = input('Yout answer: ')
        if answer == correct_answer_str:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer_str}'."
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
