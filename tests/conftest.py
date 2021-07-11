import pytest
import random

from src.Circle import Circle
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square


@pytest.fixture
def valid_circle():
    circle = Circle(random.randint(1, 10))
    yield circle
    del circle


@pytest.fixture
def valid_triangle():
    triangle = Triangle(3, 4, 5)
    yield triangle
    del triangle


@pytest.fixture
def invalid_triangle():
    not_triangle = Triangle(1, 2, 4)
    yield not_triangle
    del not_triangle


@pytest.fixture
def valid_square():
    square = Square(random.randint(1, 10))
    yield square
    del square


@pytest.fixture
def valid_rectangle():
    rectangle = Rectangle(random.randint(1, 10), random.randint(1, 10))
    yield rectangle
    del rectangle
