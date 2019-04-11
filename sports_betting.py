#####################################################
# A sports betting script written in python.
# Can learn more about a subject that can be computed
# by modeling it programmatically.
# All of the data/logic for interactive helper
# is wrapped up in an ugly function called interactive().
# It should be refactored!
# The second function, odds_calculator() accepts
# two arguments: american_odds, amount=100
# american_odds is the odds of the bet: I.e, -100, +250
# amount is the money you're wagering: i.e, 100, 275, 1000
# Returns fractional_odds, decimal_odds, to_win, payout
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
#
#####################################################

from fractions import Fraction


def interactive(option=1):
    message = """
    Type in the correct number of the input you want to learn more about:\n
    1: What does -150 and +125 mean?
    2: What does a four to one betting favorite mean?
    3: What are odds?
    4: Favorites vs Underdogs?
    5: What's a spread?
    6: EXITS out of interactive mode 
    To 'show' menu again hit 's'  
    """

    q_and_a = {
    1: """
    Let\'s assume that you’re betting on an auto race. The favorite 
    to win it is Johnny Speed, and the underdog is Tortoise Slug. 
    The favorite has the negative number attached to it so in this 
    case is Mr. Speed at -150. You'll have to bet $150 to get the 
    payout of $100, for a total of $250. 
    The underdog or Mr. Slug is +125. You'll have to bet $125 to get 
    a $100 payout which totals to $225. With underdogs you can bet 
    less money and win a higher amount. However, odds makers know 
    this and will typically pick the winners.""",
    2: """
    Typically displayed in format like 4/1. It means that for every 
    4 units you stake, you will receive one unit if you win (plus your 
    stake).
    
    More examples:
    10/1: For every 1 unit you stake, you’ll receive 10 units. 
    7/2: For every 2 units you stake, you’ll receive 7 units. 
    9/4: For every 4 units you stake, you’ll receive 9 units. 
    """,
    3: """
    A numerical expression of the likelihood that some event will occur. 
    In gambling it's typically expressed in the form of X to Y. 
    """,
    4: """
    The person or team that the odds makers predict will win. The underdog 
    is the one the odds makers predict will lose. If it's a tossup, books 
    will open as a pick. 
    """,
    5: """
    Let's assume that the Golden State Warriors are a 10-point favorite 
    (-10) against the Houston Rockets. If you bet on the warriors then they 
    need to win by 11 or more points. If the warriors win by exactly 10 
    points that's called a push and you get your original bet back. 
    On the other hand, if you bet on the Rockets plus the points (+10), 
    then you need the  Jets to either win or lose by 10 points or fewer for 
    you to win or cover your bet. 
    """,
    6: 'STOP'
    }

    count = 0

    while True:
        if count == 0:
            run = int(input(message))
            print(q_and_a.get(run))
            count += 1
        elif count > 0:
            user_input = int(input('    Enter option number:'.format()))
            if user_input == 1:
                print(q_and_a.get(user_input))
            elif user_input == 2:
                print(q_and_a.get(user_input))
            elif user_input == 3:
                print(q_and_a.get(user_input))
            elif user_input == 4:
                print(q_and_a.get(user_input))
            elif user_input == 5:
                print(q_and_a.get(user_input))
            elif user_input == 6:
                quit(1)


def odds_calculator(american_odds, amount=100):
    """provides the amount to win and the payout."""
    if american_odds > 0:
        fractional_odds = Fraction(american_odds, amount)
        to_win = int(fractional_odds * amount)
        payout = int(to_win + amount)
        decimal_odds = 1 + fractional_odds
        return fractional_odds, decimal_odds, to_win, payout
    else:
        fractional_odds = abs(Fraction(amount, american_odds))
        to_win = int(amount * fractional_odds)
        payout = int(to_win + amount)
        decimal_odds = 1 + fractional_odds
        return fractional_odds, decimal_odds, to_win, payout


if __name__ == '__main__':
    # some simple tests to get the script working
    odds = odds_calculator(-200, amount=100)
    print(odds)
