from tyred.helpers import b, g, r
from tyred.solving import find_color_path, find_path


def test_find_color_path(simple_puzzle):
    start, goal = g("A"), b("C")
    expected = [start, r("B"), goal]

    result = find_color_path(simple_puzzle, start=start, goal=goal)
    assert result == expected


def test_find_path(simple_puzzle):
    expected = [g("A"), r("B"), b("C")]
    result = find_path(simple_puzzle, start="A", goal="C")
    assert result == expected
