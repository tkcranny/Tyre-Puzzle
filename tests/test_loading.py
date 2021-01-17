from itertools import product

import networkx as nx
import pytest

from tyred.loading import PuzzleLoader, is_skippable


def test_graph_loader_gets_plain(simple_spec):
    gl = PuzzleLoader()
    result = gl._get_plain_graph(simple_spec)

    assert isinstance(result, nx.DiGraph)
    assert set(result.nodes) == {"A", "B", "C"}


def test_loads_puzzle(simple_spec):
    expected_nodes = set(product(("A", "B", "C"), ("red", "blue", "green")))
    expected_edges = {
        (("A", "green"), ("B", "red")),
        (("B", "green"), ("A", "red")),
        (("B", "red"), ("C", "blue")),
        (("C", "red"), ("B", "blue")),
    }

    gl = PuzzleLoader()
    result = gl.load_puzzle(simple_spec)

    assert set(result.nodes) == expected_nodes
    assert set(result.edges) == set(expected_edges)


def test_loads_puzzle_from_file(simple_spec_file):
    gl = PuzzleLoader()
    result = gl.load_puzzle_from_file(simple_spec_file)
    assert len(result.nodes) == 9
    assert len(result.edges) == 4


@pytest.mark.parametrize("inp", ["", "# comment"])
def test_is_skippable(inp):
    assert is_skippable(inp)
