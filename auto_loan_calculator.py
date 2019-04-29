#################################################
# Autoloan calculator
# _ _ _ _ _ _ _ _ _ _
#
# Calculates the monthly payments one will make.
# Simple script:
# Excludes other variables such as:
#   * sales tax, upfront payment, trade in value, title,
#   * registration, and other fees.
#
# A = P * (1 + r) ^N / (1 + r)^N - 1
# A = monthly payment
# P = the amount owed on a loan
# r = interest rate. Divide by 100 to represent as a decimal
# N = the term of the loan, typically represented in months.
#
# Simple Interest Equation (Principal + Interest)
#   A = P(1 + rt)
# Formula for calculating monthly interest:
# Inspired from calculator soup:
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
##################################################


def monthly_cost():
    print('Gotta couple of questions for you...')
    p = float(input('Enter loan amount '))
    r = float(input('Enter interest rate (%)'))
    n = int(input('Enter loan period (in months)'))

    # convert r to a decimal and divide by interest per year
    r = (r / 100) / 12

    # breaks formula down into 3 parts to reduce error
    # numerator
    top = r * (1 + r)**n
    # denominator
    bottom = ((1 + r)**n) - 1
    # putting it all together
    a = round(p * (top / bottom))

    # use simple interest formula
    # I = Prt
    # In this case, I = Prn
    total_interest = round(p * r * n, 3)
    print(f'Monthly costs = ${a}. Total interest = ${total_interest} ')


if __name__ == '__main__':
    monthly_cost()