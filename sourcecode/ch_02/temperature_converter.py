def fahrenheit_to_celsius():
    temp_in_fahren = float(input('Enter the temperature in Fahrenheit '))
    celsius = (temp_in_fahren - 32) * 5 / 9
    celsius = round(celsius, 4)
    print(celsius, '°C')


def fahrenheit_to_kelvin():
    temp_in_fahren = float(input('Enter the temperature in Kelvin '))
    kelvin = (temp_in_fahren - 32) / 1.8 + 273.15
    print(kelvin, 'K')


def celsius_to_fahrenheit():
    temp_in_celsius = float(input('Enter the temperature in Celsius '))
    celsius_to_fahren = (temp_in_celsius * 9 / 5) + 32
    print(celsius_to_fahren, '°F')


def celsius_to_kelvin():
    temp_in_cel = float(input('Enter the temperature in Celsius '))
    celsius_to_kel = (temp_in_cel + 273.15)
    print(celsius_to_kel, 'K')


def kelvin_to_fahrenheit():
    temp_in_kelvin = float(input('Enter the temperature in Kelvin '))
    kelvin_to_fahren = (temp_in_kelvin - 273.15) * 9 / 5 + 32
    kelvin_to_fahren = round(kelvin_to_fahren, 3)
    print(kelvin_to_fahren, '°F')


def kelvin_to_celsius():
    temp_in_kelvin = float(input('Enter the temperature in Kelvin '))
    kelvin_to_cel = temp_in_kelvin - 273.15
    kelvin_to_cel = round(kelvin_to_cel, 3)
    print(kelvin_to_cel, '°C')


if __name__ == '__main__':
    message = input("""Select one of the following options:

Type 'fc' to convert from Fahrenheit to Celsius. 
Type 'fk' to convert from Fahrenheit to Kelvin.
Type 'cf' to convert from Celsius to
 Fahrenheit.
Type 'ck' to convert from Celsius to Kelvin.
Type 'kf' to convert from Kelvin to Fahrenheit.
Type 'kc' to convert from Kelvin to Celsius.

Enter input here: 
    """)

    # casefold is for case-insensitive comparisons

    message = message.casefold()
    if message == 'fc':
        fahrenheit_to_celsius()
    elif message == 'fk':
        fahrenheit_to_kelvin()
    elif message == 'cf':
        celsius_to_fahrenheit()
    elif message == 'ck':
        celsius_to_kelvin()
    elif message == 'kf':
        kelvin_to_fahrenheit()
    elif message == 'kc':
        kelvin_to_celsius()
    else:
        print('Not a valid option pal!')