"""Tests for the word counter app."""

from app import count_words


def test_count_words_simple():
    assert count_words("hello world") == 2


def test_count_words_single():
    assert count_words("jenkins") == 1


def test_count_words_empty():
    assert count_words("") == 0
