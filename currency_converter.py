####################################################
# Simple currency converter script in python
# Converts the world's top 10 strongest global
# economies to each other.
#
# Exchange rates retrieved from exchange-rates.org
# This version of the script was written May 3, 2019.
# It doesn't update so most likely not 100% accurate by
# the time you check on it.
#
# Top 10 global economies according to FOCUS ECONOMICS:
# https://www.focus-economics.com/blog/the-largest-economies-in-the-world
# United States: Dollar -> USD
# China: Yuan -> CNH
# Japan: Japanese Yen -> JPY
# Germany: Euro -> EU
# United Kingdom: British Pound Sterling -> GBP
# India: Indian rupee -> INR
# France:  Euro -> EU
# Italy:  Euro -> EU
# Brazil: Brazilian real -> BRL
# Canada: Canadian dollar -> CAD
#
# By Doug Purcell
# http://www.purcellconsult.com
#
######################################################


def available_currencies():
    """Stores all of the currencies available"""
    currencies = {
        'United States': 'USD',
        'China': 'CNY',
        'Japan': 'JPY',
        'Germany': 'EU',
        'United Kingdom': 'GBP',
        'India': 'INR',
        'France': 'EU',
        'Italy': 'EU',
        'Brazil': 'BRL',
        'Canada': 'CAD'
    }

    for country, abbreviation in currencies.items():
        print(country, ':', abbreviation)


def america():
    """Converts from American dollar to various currencies """
    print('Convert from USD to some other currency: ')
    symbol = None
    dollars = input('Enter the currency to convert to: ').upper()
    usd_amount = float(input('Enter the amount of dollars in USD: '))
    if dollars == 'CNY':
        symbol = '¥'
        conversion = usd_amount * 6.73
    elif dollars == 'JPY':
        symbol = '¥'
        conversion = usd_amount * 111.11
    elif dollars == 'EU':
        symbol = '€'
        conversion = usd_amount * .89
    elif dollars == 'GBP':
        symbol = '£'
        conversion = usd_amount * .76
    elif dollars == 'INR':
        symbol = '₹'
        conversion = usd_amount * 69.18
    elif dollars == 'BRL':
        symbol = 'R$'
        conversion = usd_amount * 3.94
    elif dollars == 'CAD':
        symbol = '$'
        conversion = usd_amount * 1.34
    else:
        return

    print(f'{usd_amount} USD to {dollars} is {conversion} {symbol}')


def china():
    """Converts from CNY to various currencies """
    print('Convert from yuan to some other currency: ')
    symbol = None
    currency = input('Enter the currency to convert to: ').upper()
    yuans = float(input('Enter the amount of yuans: '))
    if currency == 'USD':
        symbol = '$'
        conversion = yuans * .15
    elif currency == 'JPY':
        symbol = '¥'
        conversion = yuans * 16.50
    elif currency == 'EU':
        symbol = '€'
        conversion = yuans * .13
    elif currency == 'GBP':
        symbol = '£'
        conversion = yuans * .11
    elif currency == 'INR':
        symbol = '₹'
        conversion = yuans * 10.27
    elif currency == 'BRL':
        symbol = 'R$'
        conversion = yuans * .58
    elif currency == 'CAD':
        symbol = '$'
        conversion = yuans * .20
    else:
        return
    print(f'{yuans} CNY  to {currency} is {conversion} {symbol}')


def japan():
    """Converts from yen to various currencies """
    print('Convert from yen to some other currency: ')
    symbol = None
    currency = input('Enter the currency to convert to: ').upper()
    yen = float(input('Enter the amount of yens: '))
    if currency == 'USD':
        symbol = '$'
        conversion = yen * 0.0090
    elif currency == 'CNY':
        symbol = '¥'
        conversion = yen * 0.061
    elif currency == 'EU':
        symbol = '€'
        conversion = yen * 0.0080
    elif currency == 'GBP':
        symbol = '£'
        conversion = yen * 0.0068
    elif currency == 'INR':
        symbol = '₹'
        conversion = yen * 0.62
    elif currency == 'BRL':
        symbol = 'R$'
        conversion = yen * 0.035
    elif currency == 'CAD':
        symbol = '$'
        conversion = yen * 0.012
    else:
        return
    print(f'{yen} JBY to {currency} is {conversion} {symbol}')


def euros():
    """Converts from Euros to various currencies:
    Germany, France, and Italy are under Euros.
    Therefore, doesn't make sense to convert to
    one another with this.
    THe UK is not under Euros, uses it's own currency.
    """
    print('Convert from Euro to some other currency: '
          'Germany, France, and Italy uses Euros, so '
          'can\'t convert to one another. ')
    symbol = None
    currency = input('Enter the currency to convert to: ').upper()
    euros = float(input('Enter the amount of euros: '))
    if currency == 'USD':
        symbol = '$'
        conversion = euros * 1.12
    elif currency == 'JPY':
        symbol = '¥'
        conversion = euros * 124.56
    elif currency == 'CNY':
        symbol = '¥'
        conversion = euros * 7.55
    elif currency == 'GBP':
        symbol = '£'
        conversion = euros * 0.85
    elif currency == 'INR':
        symbol = '₹'
        conversion = euros * 77.56
    elif currency == 'BRL':
        symbol = 'R$'
        conversion = euros * 4.42
    elif currency == 'CAD':
        symbol = '$'
        conversion = euros * 1.51
    else:
        return
    print(f'{euros} EU to {currency} is {conversion} {symbol}')


def the_uk():
    """Converts from british pound sterling to various currencies
    Nickname for british sterling is quid.
    """
    print('Convert from pounds to some other currency: ')
    symbol = None
    currency = input('Enter the currency to convert to: ').upper()
    british_pound = float(input('Enter the amount of pounds: '))
    if currency == 'USD':
        symbol = '$'
        conversion = british_pound * 1.32
    elif currency == 'JPY':
        symbol = '¥'
        conversion = british_pound * 146.36
    elif currency == 'CNY':
        symbol = '¥'
        conversion = british_pound * 8.87
    elif currency == 'EU':
        symbol = '€'
        conversion = british_pound * 1.17
    elif currency == 'INR':
        symbol = '₹'
        conversion = british_pound * 91.13
    elif currency == 'BRL':
        symbol = 'R$'
        conversion = british_pound * 5.19
    elif currency == 'CAD':
        symbol = '$'
        conversion = british_pound * 1.77
    else:
        return
    print(f'{british_pound} GBP to {currency} is {conversion} {symbol}')


def india():
    """Converts from India rupees to various currencies """
    print('Convert from INR to some other currency: ')
    symbol = None
    currency = input('Enter the currency to convert to: ').upper()
    indian_rupee = float(input('Enter the amount in Indian Rupees: '))
    if currency == 'USD':
        symbol = '$'
        conversion = indian_rupee * 0.014
    elif currency == 'CNY':
        symbol = '¥'
        conversion = indian_rupee * 0.097
    elif currency == 'JPY':
        symbol = '¥'
        conversion = indian_rupee * 1.61
    elif currency == 'EU':
        symbol = '€'
        conversion = indian_rupee * 0.013
    elif currency == 'GBP':
        symbol = '£'
        conversion = indian_rupee * 0.011
    elif currency == 'BRL':
        symbol = 'R$'
        conversion = indian_rupee * 0.057
    elif currency == 'CAD':
        symbol = '$'
        conversion = indian_rupee * 0.019
    else:
        return

    print(f'${indian_rupee} INR to {currency} is {conversion} {symbol}')


def brazil():
    """Converts from BRL to various currencies.
    """
    print('Convert from BRL to some other currency: ')
    symbol = None
    currency = input('Enter the currency to convert to: ').upper()
    brazilian_real = float(input('Enter the amount in Brazilian Real: '))
    if currency == 'USD':
        symbol = '$'
        conversion = brazilian_real * 0.25
    elif currency == 'CNY':
        symbol = '¥'
        conversion = brazilian_real * 1.71
    elif currency == 'JPY':
        symbol = '¥'
        conversion = brazilian_real * 28.21
    elif currency == 'EU':
        symbol = '€'
        conversion = brazilian_real * 0.23
    elif currency == 'GBP':
        symbol = '£'
        conversion = brazilian_real * 1.17
    elif currency == 'INR':
        symbol = 'R$'
        conversion = brazilian_real * 17.56
    elif currency == 'CAD':
        symbol = '$'
        conversion = brazilian_real * 0.34
    else:
        return

    print(f'${brazilian_real} BRL to {currency} is {conversion} {symbol}')


def canada():
    """Converts from CAD to various currencies.
    """
    print('Convert from CAD to some other currency: ')
    symbol = None
    currency = input('Enter the currency to convert to: ').upper()
    canadian_dollar = float(input('Enter the amount in Canadian dollars: '))
    if currency == 'USD':
        symbol = '$'
        conversion = canadian_dollar * 0.74
    elif currency == 'CNY':
        symbol = '¥'
        conversion = canadian_dollar * 5.02
    elif currency == 'JPY':
        symbol = '¥'
        conversion = canadian_dollar * 82.68
    elif currency == 'EU':
        symbol = '€'
        conversion = canadian_dollar * 0.66
    elif currency == 'GBP':
        symbol = '£'
        conversion = canadian_dollar * 0.56
    elif currency == 'BRL':
        symbol = 'R$'
        conversion = canadian_dollar * 2.93
    elif currency == 'INR':
        symbol = '$'
        conversion = canadian_dollar * 51.48
    else:
        return

    print(f'${canadian_dollar} CAD to {currency} is {conversion} {symbol}')


if __name__ == '__main__':
    print('Enter the currency you have. Provide the alphabetic code.\n'
          'I.e: USD for Dollar or JPY for yen.\n')

    countries = input('Need to see a list of countries available? Enter "y"'
                      'or "n" ').lower()
    if countries == 'y':
        available_currencies()
    else:
        print('That\'s fine :-)\n')

    code = input('Enter the alphabetic code: ').upper()
    if code == 'USD':
        america()
    elif code == 'CNY':
        china()
    elif code == 'JPY':
        japan()
    elif code == 'INR':
        india()
    elif code == 'CAD':
        canada()
    elif code == 'GBP':
        the_uk()
    elif code == 'BRL':
        brazil()
    elif code == 'EU' or code == 'BRD' or code == 'ITL' or \
            code == 'FR':
        euros()
    else:
        print('Incorrect input. Enter a correct one')