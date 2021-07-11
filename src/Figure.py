class Figure:
    area = 0

    def __new__(cls, *args):
        if cls is Figure:
            return None
        return object.__new__(cls)

    def add_area(self, other):
        if isinstance(other, Figure):
            return self.area + other.area
        else:
            raise ValueError("Should pass Figure  as parameter")
