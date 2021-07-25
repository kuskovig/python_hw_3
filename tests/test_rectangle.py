import pytest
import random

from src.Rectangle import Rectangle


def test_can_create_rectangle(valid_rectangle):
    assert isinstance(valid_rectangle, Rectangle), "Cannot create Rectangle object"
    assert valid_rectangle.name == "Rectangle", "Name of instance of Rectangle doesn't match"


def test_calculate_rectangle_area(valid_rectangle):
    assert valid_rectangle.area == valid_rectangle.first_side * valid_rectangle.second_side, \
        "Area of square is incorrect"


def test_calculate_rectangle_perimeter(valid_rectangle):
    assert valid_rectangle.perimeter == 2 * (valid_rectangle.first_side + valid_rectangle.second_side), \
        "Perimeter of rectangle is incorrect"


def test_rectangle_can_add_figures(valid_rectangle, valid_square):
    assert valid_rectangle.add_area(valid_square) == valid_rectangle.area + valid_square.area, "Summ area isn't correct"


def test_rectangle_cannot_add_to_not_figure(valid_rectangle):
    with pytest.raises(ValueError):
        assert valid_rectangle.add_area(random.randint(1, 10)), "Shouldn't be able to add with not figures"
