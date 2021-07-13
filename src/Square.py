from .Rectangle import Rectangle


class Square(Rectangle):
    name = "Square"

    def __init__(self, first_side):
        self.first_side = first_side
        self.second_side = first_side
