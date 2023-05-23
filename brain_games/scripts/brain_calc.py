#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def generate_question():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    operator = random.choice(['+', '-', '*'])
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    else:
        result = a * b
    return (f'Question: {a} {operator} {b}', result)


def get_user_answer():
    while True:
        answer = input('Your answer: ')
        try:
            answer = int(answer)
            return answer
        except ValueError:
            print('Please enter a number')


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        question, result = generate_question()
        print(question)
        answer = get_user_answer()
        if answer == result:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{result}'."
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
