"""Tests for math_utils — some of these are intentionally wrong. Fix them!"""

from math_utils import add, subtract, multiply, is_even


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    # BUG: wrong expected value
    assert multiply(3, 4) == 11


def test_is_even():
    # BUG: wrong assertion
    assert is_even(4) is False


def test_is_even_odd():
    assert is_even(7) is False
