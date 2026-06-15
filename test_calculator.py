import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(2, 6) == 12
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(9, 3) == 3.0
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
