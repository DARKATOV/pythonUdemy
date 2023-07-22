from random import *

print('Hi ! Welcome to Digital Lotery')
user_name = input('What is your name? : ')
print(f'Welcome again {user_name}. We need you to say a random number from 1 to 100. You have only 8 tries, good luck')


random_number = randint(1, 101)
print(random_number)
tries = 7

while tries >= 0:
    number = int(input('Your number? : '))
    tries -= 1

    if number == random_number and tries != 0:
        tries = 0
        print('Accomplished lol , congrats')
        answer = input('You are a winner but do you want to repeat the game? (Y/N) : ')
        if answer == 'Y':
            random_number = randint(1, 101)
            tries = 7

        else:
            print('Good choice. Thanks, bye :D')
            break

    elif number > random_number and tries != 0:
        print('The number you are looking for is smaller')
    elif number < random_number and tries != 0:
        print('The number you are looking for is greater')
    else:
        answer = input(f'You missed the train, spider. The secret number was {random_number}. Do you want to play again? (Y/N) : ')
        if answer == 'Y':
            random_number = randint(1, 101)
            tries = 7
        else:
            tries -= 1
            print('Coward. Thanks, bye :D')
