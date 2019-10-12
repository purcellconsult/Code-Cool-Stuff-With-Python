def questions():
    """This is the part of the program that prompts the user
    for a bunch of questions."""
    first_name = input('Enter your first name: ').capitalize()
    last_name = input('Enter your last name: ').capitalize()
    nationality = input('Enter your nationality: ').capitalize()
    age = int(input('Enter your age: '))
    height = input('Enter feet and inches separated by commas: ')
    user_input = height.split(',')
    heights = user_input[0], user_input[1]
    weight = float(input('Enter weight in lbs: '))
    favorite_food = input('Enter your favorite food: ').capitalize()
    favorite_city = input('Enter in your favorite city: ').capitalize()
    print()

    print('First name: {}'.format(first_name))
    print('Last name: {}'.format(last_name))
    print('Nationality: {}'.format(nationality))
    print('Age: {}'.format(age))
    print('Height: {} ft {} in'.format(user_input[0], user_input[1]))
    print('Weight: {}'.format(weight))
    print('Favorite food: {}'.format(favorite_food))
    print('Favorite city: {}'.format(favorite_city))

if __name__ == '__main__':
    # this is where your program starts
    questions()