def scale_number(num, amount):
    return num * amount
print(scale_number(10, 5))
print()

def area_triangle(height=11, width=7.5):
    return 1/2 * (height * width)
print(area_triangle())
print(area_triangle(height=20, width=100))
print()

def multiply(*args, y=1):
    for x in range(len(args)):
        y *= args[x]
    return y
print('multiply =', multiply(1, 2, 3, 4))
print()

def key_value(**kwargs):
    for key, value in kwargs.items():
        print('{} {}'.format(key, value))
key_value(a=5, b=10, c=15)
