class Point:
    """Simple class in python. This is an example
    of a docstring, or a string that's used like a
    comment to document a segment of code."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def get_point(self):
        return self.x, self.y


p = Point(5, 10)
print()
print(p.get_point())

p.set_x(100)
p.set_y(200)
print(p.get_point())