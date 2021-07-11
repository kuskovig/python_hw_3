from .Figure import Figure
import math


class Triangle(Figure):
    name = "Triangle"

    def __new__(cls, first_side, second_side, third_side):  # Check if triangle is valid, return None if not
        if (first_side + second_side <= third_side) or \
                (first_side + third_side <= second_side) or \
                (second_side + third_side <= first_side):
            return None
        else:  # return object if triangle is valid
            instance = object.__new__(cls)
            instance.first_side, instance.second_side, instance.third_side = first_side, second_side, third_side
            return instance

    @property
    def area(self):
        half_perimeter = self.perimeter / 2  # calculating area with Heron's formula
        return math.sqrt(half_perimeter * (half_perimeter - self.first_side) *
                         (half_perimeter - self.second_side) *
                         (half_perimeter - self.third_side))

    @property
    def perimeter(self):
        return self.first_side + self.second_side + self.third_side
