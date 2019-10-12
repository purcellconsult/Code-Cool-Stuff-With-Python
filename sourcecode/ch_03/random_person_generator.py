from random import randint
from random import choice
from string import ascii_letters


def first_name(male=None, female=None):
    """
    creates a random person name.
    popular male names taken from:
    https://www.babble.com/pregnancy/1000-most-popular-boy-names
    popular female names taken from: https://www.verywellfamily.com/top-1000-baby-girl-names-2757832
    popular last names: https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_North_America#United_States_(American)
    """
    genders = ['m', 'f']
    male_first_names = ['Liam', 'Noah', 'William', 'Logan', 'Benjamin', 'Mason', 'Elijah', 'Oliver', 'Jacob', 'James']
    female_first_names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Charlotte', 'Mia', 'Amelia', 'Harper', 'Evelyn']

    if male:
        name = choice(male_first_names)
        return name
    elif female:
        name = choice(female_first_names)
        return name
    elif male is None and female is None:
        pick_gender = choice(genders)
        if pick_gender == 'm':
            alias = choice(male_first_names)
            return alias
        elif pick_gender == 'f':
            alias = choice(female_first_names)
            return alias


def last_name():
    """
    generates last name
    """
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Martinez', 'Sanchez', 'Nguyen', 'Barnes']
    surname = choice(last_names)
    return surname


def full_name(male=None, female=None):
    """
    generates the full name.
    returns as string or dictionary.
    """
    email_services = ['gmail', 'aol', 'yahoo', 'aol', 'yandex', 'mail']
    create_email = input("Do you want to create an email address? Enter 'y' for yes"
                         " or 'n' for no. ").lower()

    def create_name():
        if male:
            male_name = first_name(male='m')
            last = last_name()
            full = male_name + ' ' + last
            return full
        elif female:
            female_name = first_name(female='f')
            last = last_name()
            full = female_name + ' ' + last
            return full
        else:
            first = first_name()
            last = last_name()
            full = first + ' ' + last
            return full
    if create_email == 'y':
       email_id = {
           'name': None,
           'email': None
       }
       moniker = create_name()
       first, last = moniker.split(' ')
       e_address = (first + '.' + last + '@' + choice(email_services) + '.com').lower()
       email_id['name'] = moniker
       email_id['email'] = e_address
       return email_id
    elif create_email == 'n':
        name = create_name()
        return name


def age():
    """
    creates the random person age.
    gives them a range from 1 to 100
    making the oldest possible choice a centenarian.
    """
    return randint(1, 100)


def phone_number():
    """
    creates the random person
    phone number.
    Lists valid North American
    area codes: https://en.wikipedia.org/wiki/List_of_North_American_Numbering_Plan_area_codes
    """
    number = ''
    for x in range(1, 11):
        if x == 1:
            num = randint(2, 9)
            number += str(num)
        elif x == 4:
            num = randint(2, 9)
            number += str(num)
        else:
            num = randint(0, 9)
            number += str(num)
        if x % 3 == 0 and x <= 6:
            number += '-'
    return number


def email_password(length=7):
    """
    returns a randomly generated password
    using ascii characters
    """
    return ''.join([choice(ascii_letters) for x in range(length)])


def run():
    for x in range(3):
        print(first_name())
    print()

    for x in range(3):
        print(last_name())
    print()

    for x in range(3):
        print(full_name())
    print()

    for x in range(3):
        print(age())
    print()

    for x in range(3):
        print(phone_number())
    print()

    for x in range(3):
        print(email_password())


run()
