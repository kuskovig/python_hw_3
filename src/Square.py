from .Rectangle import Rectangle


class Square(Rectangle):
    name = "Square"

    def __init__(self, first_side):
        self.first_side = first_side

    @property
    def area(self):
        return self.first_side ** 2

    @property
    def perimeter(self):
        return self.first_side * 4
