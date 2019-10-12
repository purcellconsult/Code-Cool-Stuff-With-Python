def divide(num, den):
    try:
        x = num / den
        print('{} / {} = {}'.format(num, den, num / den))
    except ZeroDivisionError:
        print("can't divide by zero.")


divide(10, 5)
divide(0, 10)
divide(10, 0)
print()


def import_test():
    try:
        import math
        import operating
        import sys
        print(math.pi)
        print(sys.version_info)
    except ImportError:
        print("Couldn't import something")
import_test()


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Can't divide by 0")
    else:
        print(result)
    finally:
        print('This is in the finally statement')
divide(10, 2)

try:
    a = input('Enter an integer ')
    raise Exception("Something strange happened")
except ValueError:
    print("An exception happened.")