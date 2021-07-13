import pytest
import random

from src.Square import Square


def test_can_create_square(valid_square):
    assert isinstance(valid_square, Square), "Cannot create Square object"
    assert valid_square.name == "Square", "Name of instance of Square doesn't match"


def test_calculate_square_area(valid_square):
    assert valid_square.area == valid_square.first_side * valid_square.second_side, "Area of square is incorrect"


def test_calculate_square_perimeter(valid_square):
    assert valid_square.perimeter == 2 * (valid_square.first_side + valid_square.second_side),\
        "Perimeter of square is incorrect"


def test_square_can_add_figures(valid_square, valid_triangle):
    assert valid_square.add_area(valid_triangle) == valid_square.area + valid_triangle.area, "Summ area isn't correct"


def test_square_cannot_add_to_not_figure(valid_square):
    with pytest.raises(ValueError):
        assert valid_square.add_area(random.randint(1, 10)), "Shouldn't be able to add with not figures"
