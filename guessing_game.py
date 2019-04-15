#######################################
# A text based word guessing game script
# in python.
#
# Once script runs, the word is revealed
# using asterisk ['*', '*', *', '*']
#
# Then, the user can guess a letter
# or guess the entire word. Feedback will
# be provided on each input the user enters.
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
########################################

import random


def generate_word():
    words = ['hello', 'baby', 'apple', 'tuna', 'macbook']

    # picks a word in the range of 4-9
    pick = True
    while pick:
        if len(words) > 4 < 10:
            pick_word = random.choice(words)
            pick = False
        else:
            pass
    return pick_word


def build_word():
    """builds the word builds the word in a
    list called build_word"""
    pick_word = generate_word()
    word = []
    for x in pick_word:
        word.append(x)
    return word


def build_stars():
    """generate a list of stars that's the same
    size as word."""
    word = build_word()
    size = len(word)
    # builds a list of stars that have same size as build_word
    stars = []
    i = 0
    while i < size:
        stars.append('*')
        i += 1
    return stars


def main():
    """the main logic of the game."""
    word = build_word()
    stars = build_stars()
    tries = len(word) + 2
    i = 0
    while i < tries:
        print(stars)
        your_guess = input('Guess a letter: ')
        i += 1
        j = 0
        while j < len(word):
            if your_guess == word[j]:
                stars[j] = your_guess
                print('CORRECT! {} is in the word.'.format(your_guess))
                print(stars)
            j += 1
        if your_guess == ''.join(word):
            print('CORRECT!')
            break
        if word == stars:
            print('you win!')
            break
        if word != stars and i == tries:
            print('GAME OVER!')
        print('You have {} tries left'.format(tries - i))


if __name__ == '__main__':
    main()


