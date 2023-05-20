#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
    return name


def generate_progression(length):
    first_num = random.randint(1, 10)
    diff = random.randint(1, 10)
    return [first_num + i * diff for i in range(length)]


def hidden_num(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, hidden_index, hidden_value


def check_answer(answer, hidden_value):
    try:
        if int(answer) == hidden_value:
            return True
        else:
            return False
    except ValueError:
        return False


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    for _ in range(3):
        length = random.randint(10, 15)
        progression = generate_progression(length)
        with_hidden_num, hidden_index, hidden_value = hidden_num(progression)
        print('Question:', ' '.join(map(str, with_hidden_num)))
        answer = prompt.string('Your answer: ')
        if check_answer(answer, hidden_value):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.\
Correct answer was '{hidden_value}'. Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
