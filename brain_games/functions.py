#!/usr/bin/env python

import prompt
from random import randint


def is_even():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no".')
    for i in range(0,3):
        random_number = randint(1,100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
            else:
                print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'yes\'')
                print(f'Let\'s try again, {name}')
                break
        else:
            if answer == 'no':
                print('Correct!')
            else:
                print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'no\'')
                print(f'Let\'s try again, {name}')
                break
        if i == 2:
            print(f'Congratulations, {name}!')
