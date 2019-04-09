#######################################################
# This simple script allows you to generate a
# random password in the range of 6-128 chars.
# Below is an example input/output:
#
# >>> The password's length must be in range 6-128 chars: 10
# C#'.1o_Jo2
#
# By Doug Purcell
# Website: http://www.purcellconsult.com
#
#######################################################

import string
import random


def settings():
    """"Asks questions to modify the customer's
    settings for the password security.
    """

    password_length = int(input('The password\'s length must be in range 6-128 '
                                'chars: '))

    if password_length >= 6 <= 128:
        pass
    else:
        raise Exception('Invalid entries.')
    special_characters, letters, numbers = string.punctuation, string.ascii_letters, string.digits
    all_chars = []
    all_chars.extend(special_characters)
    all_chars.extend(letters)
    all_chars.extend(numbers)
    return all_chars, password_length


def build_password():
    """This function builds the actual string."""
    random_chars, size = settings()  # gets the two returned values from settings
    password = ''
    i = 0
    while i < size:
        char = random.choice(random_chars)
        password += char
        i += 1
    return password


if __name__ == '__main__':
    print(build_password())
