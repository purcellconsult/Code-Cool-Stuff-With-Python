##########################################################
# Spanish translator in python
# A simple script that translates
# popular Mexican foods from Spanish
# to English, and common phrases from English
# to Spanish:
#
# To use script simply type: python spanish_translator.py
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
###########################################################


def food():
    """Names for some popular mexican food items.
    Translate spanish food names to english.
    """
    print('\n')
    spanish_to_english = {
        'Birria': 'Spicy stew made with goat or mutton. ',
        'Quesadilla con carne': 'season steak strips. ',
        'Barbacoa': 'Slow cooked meat in soup. Beef, goat, or sheep.',
        'Burrito Banado': 'Wet Burrito.',
        'Huevos rancheros': '"Rancher\'s eggs." Corn tortillas, fried eggs, topped with warm salsa.',
        'Coctel de camarones': 'Shrimp cocktail served cold with tomato, onion, cucumber, and cilantro. ',
        'Huevos a la mexicana': 'Eggs, tomato, onion, and serrano chile. A classic.',
        'Huevo con Chorizo': 'Eggs and chorizo sausage.',
        'Burritos de Desayuno ': 'Breakfast burrito.',
        'Chilli con carne': 'Chili with meat.',
        'Lengua': 'Beef tongue, typically in tacos.',
        'Tripas': 'Small intestines of farm animals that\'s cleaned, boiled, and grilled. ',
        'Al pastor': 'Pork based taco based on shawarma',
        'Suadero': 'Tender slow cooked beef brisket. Typically served in tacos.',
        'Cabeza': 'Beef head/cheek meat. Served in soups or tacos.',
        'Sesos': 'Brains from either a goat or cow. Popular taco filling.'
    }

    print('Spanish phases available for translation:')
    for spanish, english in spanish_to_english.items():
        print(spanish)

    print()
    translate = input('Type in spanish phase you\'ll like to translate: ').capitalize()
    for english, spanish in spanish_to_english.items():
        if translate == english:
            print(spanish_to_english.get(translate))
            break
    else:
        print('Word is not available for translation')


def general_phases():
    """Shows available english phases, and then translates
    appropriately.
    """
    print('\n')
    english_to_spanish = {
        'Hello': '¡Hola! ',
        'Please': 'Por favor',
        'Thank you': 'Gracias',
        'Where is the bathroom?': '¿Dónde está  el baño?',
        'I\'m sorry': 'Lo siento',
        'Do you speak English?': '¿Habla usted Inglés?',
        'I don\'t speak much Spanish': 'No hablo mucho español?',
        'I don\'t know': 'No sé',
        'Clear': 'Claro',
        'Good-bye': 'Adiós',
    }

    print('English phases available for translation:')
    for english, spanish in english_to_spanish.items():
        print(english)

    print()
    translate = input('Type English phase to translate to Espanol: ')
    translate = translate.capitalize()
    for english, spanish in english_to_spanish.items():
        if translate == english:
            print(english_to_spanish.get(translate))
            break
    else:
        print('Word is not available for translation')


if __name__ == '__main__':

    print('Bienvenidos! What phases would you like to translate?')
    print('1: Common foods ')
    print('2: General phases')
    your_choice = int(input("Enter your choice: '1' or '2'"))
    if your_choice == 1:
        food()
    elif your_choice == 2:
        general_phases()
    else:
        print('Not a possible choice!')
