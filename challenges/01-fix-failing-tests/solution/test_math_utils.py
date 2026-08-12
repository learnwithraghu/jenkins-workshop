"""Tests for math_utils — corrected version."""

from math_utils import add, subtract, multiply, is_even


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_is_even():
    assert is_even(4) is True


def test_is_even_odd():
    assert is_even(7) is False
