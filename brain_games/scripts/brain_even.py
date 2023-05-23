#!/usr/bin/env python3
from random import randint
import prompt
# считаем остаток от деления, узнаем четное или нечетное


def is_even(num):
    return num % 2 == 0


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    success = True
    for _ in range(3):  # указываю что всего 3 раунда
        num = randint(1, 100)  # ноль не может быть загадан
        print(f'Question: {num}')
        answer = input('Your answer: ')
        # пишем условия для правильных ответов
        # пришлось делать перенос через обратный слэш
        if (is_even(num) and answer == 'yes') \
                or (not is_even(num) and answer == 'no'):
            print('Correct!')
        # пишем условия неправильного ответа и прирываем командой break
        # сделал перенос при помощи f-строки
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"{'yes' if is_even(num) else 'no'}.")
            print(f"Let's try again, {name}!")
            success = False
            break
    # если без ошибок ответили, то выводим поздравление игроку
    if success:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
