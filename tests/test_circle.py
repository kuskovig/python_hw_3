import random
import pytest
import math

from src.Circle import Circle


def test_can_create_circle(valid_circle):
    assert isinstance(valid_circle, Circle), "Cannot create Circle object"
    assert valid_circle.name == "Circle", "Name of instance of Circle doesn't match"


def test_calculate_circle_area(valid_circle):
    assert valid_circle.area == math.pi * valid_circle.radius ** 2, "Area of circle is incorrect"


def test_calculate_circle_perimeter(valid_circle):
    assert valid_circle.perimeter == math.pi * 2 * valid_circle.radius


def test_circle_can_add_figures(valid_circle, valid_square):
    assert valid_circle.add_area(valid_square) == valid_circle.area + valid_square.area, "Summ area isn't correct"


def test_circle_cannot_add_to_not_figure(valid_circle):
    with pytest.raises(ValueError):
        assert valid_circle.add_area(random.randint(1, 10)), "Shouldn't be able to add with not figures"
