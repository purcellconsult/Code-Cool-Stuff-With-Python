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
    'snow', 'snow2', 'snow3', 'snow4','ghostwhite', 'whitesmoke',
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
    the list.
    """
    x = randint(0, number_of_colors()-1)
    return turtle_colors[x]






