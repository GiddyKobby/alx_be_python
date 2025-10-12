# polymorphism_demo.py
import math

class Shape:
    """Base class representing a geometric shape."""
    def area(self):
        """Method to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle: length × width"""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of a circle: π × radius²"""
        return math.pi * (self.radius ** 2)

