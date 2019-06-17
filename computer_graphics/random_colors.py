####################################################################
# Random color generator with turtle
# Enjoy 150 colors that you can use in
# your python computer graphics!
#
# Taken from: https://ecsdtech.com/8-pages/121-python-turtle-colors
#
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#####################################################################

from random import randint

turtle_colors = [
    'snow', 'snow2', 'snow3', 'snow4', 'ghostwhite', 'whitesmoke',
    'gainsboro', 'floralwhite', 'oldlace', 'linen', 'antiquewhite',
    'antiquewhite2', 'antiquewhite2', 'antiquewhite3', 'antiquewhite4',
    'papayawhip', 'blanchedalmond','bisque', 'bisque2', 'bisque3', 'bisque4',
    'peachpuff', 'peachpuff2', 'peachpuff3', 'peachpuff4',
    'navajowhite', 'moccasin', 'cornsilk','cornsilk2','cornsilk3',
    'cornsilk4', 'ivory','ivory2', 'ivory3', 'ivory4', 'lemonchiffon',
    'seashell', 'seashell2', 'seashell3', 'seashell4', 'honeydew',
    'honeydew2', 'honeydew3', 'honeydew4', 'mintcream','azure',
    'aliceblue', 'lavender', 'lavenderblush', 'mistyrose', 'white',
    'black', 'darkslategray', 'dimgray', 'slategray', 'lightslategray',
    'gray', 'lightgray', 'midnightblue', 'navy', 'cornflowerblue',
    'darkslateblue', 'slateblue', 'mediumslateblue', 'lightslateblue',
    'mediumslateblue', 'lightslateblue', 'mediumblue', 'royalblue',
    'blue', 'dodgerblue', 'deepskyblue', 'skyblue', 'lightskyblue',
    'lightblue', 'powderblue', 'paleturquoise', 'darkturquoise',
    'mediumturquoise', 'turquoise', 'cyan', 'lightcyan','cadetblue',
    'mediumaquamarine', 'aquamarine', 'darkgreen', 'darkolivegreen',
    'darkseagreen', 'seagreen', 'mediumseagreen', 'lightseagreen',
    'palegreen', 'springgreen', 'lawngreen', 'chartreuse',
    'mediumspringgreen', 'greenyellow', 'limegreen', 'yellowgreen',
    'forestgreen', 'olivedrab', 'darkkhaki', 'khaki', 'palegoldenrod',
    'lightgoldenrodyellow', 'lightyellow', 'yellow', 'gold', 'lightgoldenrod',
    'goldenrod', 'darkgoldenrod', 'rosybrown', 'indianred', 'saddlebrown',
    'sienna', 'peru', 'burlywood', 'beige', 'wheat', 'sandybrown', 'tan',
    'chocolate', 'firebrick', 'brown', 'darksalmon', 'orange', 'darkorange',
    'coral', 'lightcoral', 'tomato', 'orangered', 'red', 'hotpink', 'deeppink',
    'pink', 'lightpink', 'palevioletred', 'maroon', 'mediumvioletred', 'violetred',
    'violet', 'plum', 'orchid', 'mediumorchid', 'darkorchid', 'darkviolet',
    'blueviolet', 'purple', 'mediumpurple', 'thistle'

]


def number_of_colors():
    """
    gets the total number of
    colors available.
    """
    return len(turtle_colors)


def get_random_color():
    """
    returns a random color from
    all of the 150 options.
    """
    x = randint(0, number_of_colors()-1)
    return turtle_colors[x]

"""
Use the following functions if
you want to only return colors from
a similar shade 
"""


def whites_and_pastels():
    """
    gets a light color such as
    snow or cornsilk
    """
    x = randint(0, 50)
    return turtle_colors[x]


def grays():
    """
    returns colors from black
    to light gray
    """
    x = randint(51, 56)
    return turtle_colors[x]


def blues():
    """
    returns shades of blue.
    """
    x = randint(58, 83)
    return turtle_colors[x]


def greens():
    """
    returns shades of green.
    """
    x = randint(83, 103)
    return turtle_colors[x]


def yellows():
    """
    returns shades of yellow
    """
    x = randint(103, 110)
    return turtle_colors[x]


def browns():
    """
    returns shades of brown
    """
    x = randint(110, 123)
    return turtle_colors[x]


def oranges():
    """
    returns shades of orange.
    """
    x = randint(123, 131)
    return turtle_colors[x]


def pinks_violets():
    """
    returns shades of pink and violets.
    """
    x = randint(131, 151)
    return turtle_colors[x]






