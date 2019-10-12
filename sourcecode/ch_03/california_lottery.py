
from random import randint
from time import sleep


def daily_3():
    """
    emulates the daily 3
    lottery
    """
    print("Welcome! You're playing Daily 3.")
    lucky_one = randint(0, 9)
    lucky_two = randint(0, 9)
    lucky_three = randint(0, 9)

    guess_one = int(input('Guess your lucky number: 0 - 9 '))
    guess_two = int(input('Guess your lucky number: 0 - 9 '))
    guess_three = int(input('Guess your lucky number: 0 - 9 '))

    print("Here's the Daily 3 results...")
    sleep(3)
    print(lucky_one)
    sleep(2)
    print(lucky_two)
    sleep(2)
    print(lucky_three)
    print([lucky_one,lucky_two, lucky_three])

    if guess_one == lucky_one and guess_two == lucky_two and guess_three == lucky_three:
        print("Congrats! You won $500")
    else:
        print("Today wasn't your day! Try again.")


def daily_4():
    """
    emulates the daily 4
    lottery
    """
    print("Welcome! You're playing Daily 4.")
    lucky_one = randint(0, 9)
    lucky_two = randint(0, 9)
    lucky_three = randint(0, 9)
    lucky_four = randint(0, 9)

    guess_one = int(input('Guess your lucky number: 0 - 9 '))
    guess_two = int(input('Guess your lucky number: 0 - 9 '))
    guess_three = int(input('Guess your lucky number: 0 - 9 '))
    guess_four = int(input('Guess your lucky number: 0 - 9 '))

    print("Here's the Daily 4 results...")
    sleep(3)
    print(lucky_one)
    sleep(2)
    print(lucky_two)
    sleep(2)
    print(lucky_three)
    sleep(2)
    print(lucky_four)

    print([lucky_one, lucky_two, lucky_three, lucky_four])

    if guess_one == lucky_one and guess_two == lucky_two and guess_three == lucky_three and guess_four == lucky_four:
        print("Congrats! You won the jackpot")
    else:
        print("Today wasn't your day! Try again.")


def fantasy_5():
    """
    fantasy 5 are 5 numbers within the range
    of 1-39.
    """
    print("Welcome! You're playing Fantasy 5.")
    lucky_one = randint(1, 39)
    lucky_two = randint(1, 39)
    lucky_three = randint(1, 39)
    lucky_four = randint(1, 39)
    lucky_five = randint(1, 39)

    guess_one = int(input('Guess your lucky number: 1 - 39 '))
    guess_two = int(input('Guess your lucky number: 1 - 39 '))
    guess_three = int(input('Guess your lucky number: 1 - 39 '))
    guess_four = int(input('Guess your lucky number: 1 - 39 '))
    guess_five = int(input('Guess your lucky number: 1 - 39 '))

    print("Here's the Fantasy 5 results...")
    sleep(3)
    print(lucky_one)
    sleep(2)
    print(lucky_two)
    sleep(2)
    print(lucky_three)
    sleep(2)
    print(lucky_four)
    sleep(2)
    print(lucky_five)

    print([lucky_one, lucky_two, lucky_three, lucky_four, lucky_five])

    if guess_one == lucky_one and guess_two == lucky_two and \
            guess_three == lucky_three and guess_four == lucky_four\
            and guess_five == lucky_five:
        print("Congrats! You won the jackpot")
    else:
        print("Today wasn't your day! Try again.")


def super_lotto_plus():
    """
    Pick any five numbers within the range of
    1-47, and then one omega number within the
    range of 1-27.
    """
    print("Welcome! You're playing Super Lotto Plus.")
    lucky_one = randint(1, 47)
    lucky_two = randint(1, 47)
    lucky_three = randint(1, 47)
    lucky_four = randint(1, 47)
    lucky_five = randint(1, 47)
    lucky_six = randint(1, 27)

    guess_one = int(input('Guess your lucky number: 1 - 47 '))
    guess_two = int(input('Guess your lucky number: 1 - 47 '))
    guess_three = int(input('Guess your lucky number: 1 - 47 '))
    guess_four = int(input('Guess your lucky number: 1 - 47 '))
    guess_five = int(input('Guess your lucky number: 1 - 47 '))
    guess_six = int(input('Guess your mega number: 1 - 27 '))

    print("Here's the Super Lotto Plus results...")
    sleep(3)
    print(lucky_one)
    sleep(2)
    print(lucky_two)
    sleep(2)
    print(lucky_three)
    sleep(2)
    print(lucky_four)
    sleep(2)
    print(lucky_five)
    sleep(2)
    print(lucky_six)

    print([lucky_one, lucky_two, lucky_three, lucky_four, lucky_five, lucky_six])

    if guess_one == lucky_one and guess_two == lucky_two and \
            guess_three == lucky_three and guess_four == lucky_four \
            and guess_five == lucky_five and guess_six == lucky_six:
        print("Congrats! You won the jackpot")
    else:
        print("Today wasn't your day! Try again.")


def mega_millions():
    """
    5 numbers from 1-70, and 1 number from 1-25.
    """
    print("Welcome! You're playing Mega Millions.")
    lucky_one = randint(1, 70)
    lucky_two = randint(1, 70)
    lucky_three = randint(1, 70)
    lucky_four = randint(1, 70)
    lucky_five = randint(1, 70)
    lucky_six = randint(1, 26)

    guess_one = int(input('Guess your lucky number: 1 - 70 '))
    guess_two = int(input('Guess your lucky number: 1 - 70 '))
    guess_three = int(input('Guess your lucky number: 1 - 70 '))
    guess_four = int(input('Guess your lucky number: 1 - 70 '))
    guess_five = int(input('Guess your lucky number: 1 - 70 '))
    guess_six = int(input('Guess your mega number: 1 - 26 '))

    print("Here's the Mega Million results...")
    sleep(3)
    print(lucky_one)
    sleep(2)
    print(lucky_two)
    sleep(2)
    print(lucky_three)
    sleep(2)
    print(lucky_four)
    sleep(2)
    print(lucky_five)
    sleep(2)
    print(lucky_six)

    print([lucky_one, lucky_two, lucky_three, lucky_four, lucky_five, lucky_six])

    if guess_one == lucky_one and guess_two == lucky_two and \
            guess_three == lucky_three and guess_four == lucky_four \
            and guess_five == lucky_five and guess_six == lucky_six:
        print("Congrats! You won the jackpot")
    else:
        print("Today wasn't your day! Try again.")


def powerball():
    print("Welcome! You're playing Powerball.")
    lucky_one = randint(1, 69)
    lucky_two = randint(1, 69)
    lucky_three = randint(1, 69)
    lucky_four = randint(1, 69)
    lucky_five = randint(1, 69)
    lucky_six = randint(1, 26)

    guess_one = int(input('Guess your lucky number: 1 - 69 '))
    guess_two = int(input('Guess your lucky number: 1 - 69 '))
    guess_three = int(input('Guess your lucky number: 1 - 69 '))
    guess_four = int(input('Guess your lucky number: 1 - 69 '))
    guess_five = int(input('Guess your lucky number: 1 - 69 '))
    guess_six = int(input('Guess the powerball: 1 - 26 '))

    print("Here's the Powerball results...")
    sleep(3)
    print(lucky_one)
    sleep(2)
    print(lucky_two)
    sleep(2)
    print(lucky_three)
    sleep(2)
    print(lucky_four)
    sleep(2)
    print(lucky_five)
    print('And thee powerball...')
    sleep(5)
    print(lucky_six)

    print([lucky_one, lucky_two, lucky_three, lucky_four, lucky_five, lucky_six])

    if guess_one == lucky_one and guess_two == lucky_two and \
            guess_three == lucky_three and guess_four == lucky_four \
            and guess_five == lucky_five and guess_six == lucky_six:
        print("Congrats! You won the jackpot")
    else:
        print("Today wasn't your day! Try again.")


if __name__ == '__main__':
    daily_3()