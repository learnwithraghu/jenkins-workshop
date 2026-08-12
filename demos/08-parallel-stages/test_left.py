"""Unit A tests — runs in one parallel branch."""


def test_string_upper():
    assert "jenkins".upper() == "JENKINS"


def test_list_length():
    assert len([1, 2, 3]) == 3
