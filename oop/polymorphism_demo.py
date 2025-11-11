import math

class Shape:
    """Base class representing a geometric shape."""

    def area(self):
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
