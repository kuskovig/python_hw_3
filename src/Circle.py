from .Figure import Figure
import math


class Circle(Figure):
    name = "Circle"

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return math.pi * 2 * self.radius
