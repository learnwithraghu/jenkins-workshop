"""Unit B tests — runs in the other parallel branch."""


def test_sum():
    assert sum([1, 2, 3, 4]) == 10


def test_dict_lookup():
    tools = {"ci": "jenkins"}
    assert tools["ci"] == "jenkins"
