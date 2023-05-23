#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def generate_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    return a, b


def result(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        a, b = generate_question()
        print(f'Question: {a} {b}')
        answer = input('Your answer: ')
        correct_answer = str(result(a, b))
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.\
             Correct answer was '{correct_answer}'. Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
