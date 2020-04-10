"""
A very non-efficient way to randomly draw numbers
and print unique output each time.  
"""

from random import choice


def straight_bet(games=3, nums=9):
    cycles = games
    pass_nums = []
    roll = [x for x in range(nums + 1)]
    while cycles > 0:
        rand_one = choice(roll)
        rand_two = choice(roll)
        rand_three = choice(roll)
        if rand_one in pass_nums or rand_one == rand_two or rand_one == rand_three:
            continue
        elif rand_two in pass_nums or rand_two == rand_three:
            continue
        elif rand_three in pass_nums:
            continue
        else:
            cycles -= 1
            print('{} {} {}'.format(rand_one, rand_two, rand_three))
            pass_nums.append(rand_one)
            pass_nums.append(rand_two)
            pass_nums.append(rand_three)
            roll.remove(rand_one)
            roll.remove(rand_two)
            roll.remove(rand_three)


straight_bet()