import pytest
import random
import math

from src.Triangle import Triangle


def test_can_create_valid_triangle(valid_triangle):
    assert isinstance(valid_triangle, Triangle), "Cannot create Triangle object"
    assert valid_triangle.name == "Triangle", "Name of instance of Triangle doesn't match"


def test_cannot_create_invalid_triangle(invalid_triangle):
    assert invalid_triangle is None, "Shouldn't be able to create invalid triangle "


def test_calculate_triangle_area(valid_triangle):  # using .perimeter method as it used to calculate area property
    half_perimeter = valid_triangle.perimeter / 2
    assert valid_triangle.area == math.sqrt(half_perimeter * (half_perimeter - valid_triangle.first_side) *
                                            (half_perimeter - valid_triangle.second_side) *
                                            (half_perimeter - valid_triangle.third_side)), "Area of triangle is " \
                                                                                           "incorrect (could be " \
                                                                                           "caused by broken " \
                                                                                           ".perimeter method "


def test_calculate_triangle_perimeter(valid_triangle):
    assert valid_triangle.perimeter == valid_triangle.first_side + \
           valid_triangle.second_side + valid_triangle.third_side, "Perimeter of triangle is incorrect"


def test_triangle_can_add_figures(valid_triangle, valid_circle):
    assert valid_triangle.add_area(valid_circle) == valid_triangle.area + valid_circle.area, "Summ area isn't correct"


def test_triangle_cannot_add_to_not_figure(valid_triangle):
    with pytest.raises(ValueError):
        assert valid_triangle.add_area(random.randint(1, 10))
